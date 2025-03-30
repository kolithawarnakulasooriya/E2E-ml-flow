import unittest
from unittest.mock import patch, Mock
from zipfile import ZipFile
import os
from src.data_injester.zip_data_ingester import ZipDataIngester

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

    @patch('src.data_injester.zip_data_ingester.ZipFile')
    def test_multiple_csv_files(self, mock_zipfile):
        data_ingester = ZipDataIngester()

        with patch('os.listdir') as mocked_listdir:
            mocked_listdir.return_value = ['file1.csv', 'file2.csv']
            self.assertRaises(ValueError, data_ingester.ingest, "abc.zip")

if __name__ == '__main__':
    unittest.main()