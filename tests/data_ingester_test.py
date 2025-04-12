import unittest
from unittest.mock import patch, Mock
from zipfile import ZipFile
import pandas as pd
from src.core.data_ingesting import DataIngestFactory, ZipDataIngest
from pandas.testing import assert_frame_equal

class TestZipDataIngest(unittest.TestCase):

    def test_file_not_zip(self):
        data_ingest = ZipDataIngest()
        self.assertRaises(ValueError, data_ingest.ingest, "abc.zipp")

    @patch('src.core.data_ingesting.ZipFile')
    def test_no_csv_files(self, mock_zipfile):
        data_ingest = ZipDataIngest()
        
        with patch('os.listdir') as mocked_listdir:
            mocked_listdir.return_value = []
            self.assertRaises(FileNotFoundError, data_ingest.ingest, "abc.zip")
            mocked_listdir.assert_called_once()
            mock_zipfile.assert_called_once()

    @patch('src.core.data_ingesting.ZipFile')
    def test_multiple_csv_files(self, mock_zipfile):
        data_ingest = ZipDataIngest()

        with patch('os.listdir') as mocked_listdir:
            mocked_listdir.return_value = ['file1.csv', 'file2.csv']
            
            self.assertRaises(ValueError, data_ingest.ingest, "abc.zip")
            mocked_listdir.assert_called_once()
            mock_zipfile.assert_called_once()

    @patch('pandas.read_csv')
    @patch('src.core.data_ingesting.ZipFile') 
    def test_csv_file_with_dataframe(self, mock_zipfile, mock_pd):
        data_ingest = ZipDataIngest()

        with patch('os.listdir') as mocked_listdir:
            with patch('os.path.join') as mocked_join:
                mocked_listdir.return_value = ['file1.csv']
                mocked_join.return_value = ''
                mock_df = pd.DataFrame({})
                mock_pd.return_value = mock_df
                df = data_ingest.ingest('abs.zip')
                mocked_listdir.assert_called_once()
                mocked_join.assert_called_once()
                mock_pd.assert_called_once()
                mock_zipfile.assert_called_once()
                assert_frame_equal(df, mock_df)

    @patch('pandas.read_csv')
    @patch('src.core.data_ingesting.ZipFile') 
    def test_exact_csv_file_with_dataframe(self, mock_zipfile, mock_pd):
        data_ingest = ZipDataIngest()

        with patch('os.listdir') as mocked_listdir:
            with patch('os.path.join') as mocked_join:
                mocked_listdir.return_value = ['file1.csv','file2.csv']
                mocked_join.return_value = ''
                mock_df = pd.DataFrame({})
                mock_pd.return_value = mock_df
                df = data_ingest.ingest('abs.zip',exact_csv='file2.csv')
                mocked_listdir.assert_called_once()
                mocked_join.assert_called_with("data/extracted",'file2.csv')
                mock_pd.assert_called_once()
                mock_zipfile.assert_called_once()
                assert_frame_equal(df, mock_df)

    @patch('src.core.data_ingesting.ZipFile')
    def test_exact_csv_not_found_files(self, mock_zipfile):
        data_ingest = ZipDataIngest()

        with patch('os.listdir') as mocked_listdir:
            mocked_listdir.return_value = ['file1.csv', 'file2.csv']
            
            self.assertRaises(ValueError, data_ingest.ingest, "abc.zip", 'file3.csv')
            mocked_listdir.assert_called_once()
            mock_zipfile.assert_called_once()

class TestDataIngestFactory(unittest.TestCase):
    
    @patch('src.core.data_ingesting.ZipDataIngest')
    def test_factory_get_data_ingest_zip(self, zip_ingest):
        m = Mock()
        zip_ingest.return_value = m

        self.assertEqual(DataIngestFactory.get_data_ingest('.zip'), m)

    def test_factory_get_data_ingest_invalid(self):
        self.assertRaises(ValueError, DataIngestFactory.get_data_ingest, 'N')

if __name__ == '__main__':
    unittest.main()