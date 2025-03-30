import unittest
from unittest.mock import patch, Mock
from zipfile import ZipFile
import pandas as pd
from src.data_injester.zip_data_ingester import ZipDataIngester
from src.data_injester.data_ingester_factory import DataIngesterFactory
from pandas.testing import assert_frame_equal

class TestZipDataIngester(unittest.TestCase):

    def test_file_not_zip(self):
        data_ingester = ZipDataIngester()
        self.assertRaises(ValueError, data_ingester.ingest, "abc.zipp")

    @patch('src.data_injester.zip_data_ingester.ZipFile')
    def test_no_csv_files(self, mock_zipfile):
        data_ingester = ZipDataIngester()
        
        with patch('os.listdir') as mocked_listdir:
            mocked_listdir.return_value = []
            self.assertRaises(FileNotFoundError, data_ingester.ingest, "abc.zip")
            mocked_listdir.assert_called_once()
            mock_zipfile.assert_called_once()

    @patch('src.data_injester.zip_data_ingester.ZipFile')
    def test_multiple_csv_files(self, mock_zipfile):
        data_ingester = ZipDataIngester()

        with patch('os.listdir') as mocked_listdir:
            mocked_listdir.return_value = ['file1.csv', 'file2.csv']
            
            self.assertRaises(ValueError, data_ingester.ingest, "abc.zip")
            mocked_listdir.assert_called_once()
            mock_zipfile.assert_called_once()

    @patch('pandas.read_csv')
    @patch('src.data_injester.zip_data_ingester.ZipFile') 
    def test_csv_file_with_dataframe(self, mock_zipfile, mock_pd):
        data_ingester = ZipDataIngester()

        with patch('os.listdir') as mocked_listdir:
            with patch('os.path.join') as mocked_join:
                mocked_listdir.return_value = ['file1.csv']
                mocked_join.return_value = ''
                mock_df = pd.DataFrame({})
                mock_pd.return_value = mock_df
                df = data_ingester.ingest('abs.zip')
                mocked_listdir.assert_called_once()
                mocked_join.assert_called_once()
                mock_pd.assert_called_once()
                mock_zipfile.assert_called_once()
                assert_frame_equal(df, mock_df)

    @patch('src.data_injester.data_ingester_factory.ZipDataIngester')
    def test_factory_get_data_ingester_zip(self, zip_ingester):
        m = Mock()
        zip_ingester.return_value = m

        self.assertEqual(DataIngesterFactory.get_data_ingester('.zip'), m)

    def test_factory_get_data_ingester_invalie(self):
        self.assertRaises(ValueError, DataIngesterFactory.get_data_ingester, 'N')

if __name__ == '__main__':
    unittest.main()