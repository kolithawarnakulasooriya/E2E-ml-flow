import unittest
import pandas as pd
from unittest.mock import patch
from src.analysis.varient_analysis import NumericalUnivarientAnalyzer, CategoricalUnivarientAnalyzer

class TestNumericalUnivarientAnalyzer(unittest.TestCase):

    @patch('src.analysis.varient_analysis.plt.figure')
    @patch('src.analysis.varient_analysis.plt.title')
    @patch('src.analysis.varient_analysis.plt.xlabel')
    @patch('src.analysis.varient_analysis.plt.ylabel')
    @patch('src.analysis.varient_analysis.plt.show')
    @patch('src.analysis.varient_analysis.histplot')
    def test_analyse(self, mock_figure, mock_title, mocl_x_label, mock_y_label, mock_show, mock_sns):
        strategy = NumericalUnivarientAnalyzer()
        df = pd.DataFrame({'test': [1], 'name': ['test1']})
        strategy.setOptions('test').analyse(df)
        self.assertTrue(True)
        mock_figure.assert_called()
        mock_title.assert_called()
        mocl_x_label.assert_called()
        mock_y_label.assert_called()
        mock_show.assert_called()
        mock_sns.assert_called()

class TestCategoricalUnivarientAnalyzer(unittest.TestCase):

    @patch('src.analysis.varient_analysis.plt.figure')
    @patch('src.analysis.varient_analysis.plt.title')
    @patch('src.analysis.varient_analysis.plt.xlabel')
    @patch('src.analysis.varient_analysis.plt.ylabel')
    @patch('src.analysis.varient_analysis.plt.show')
    @patch('src.analysis.varient_analysis.countplot')
    def test_analyse(self, mock_figure, mock_title, mocl_x_label, mock_y_label, mock_show, mock_sns):
        strategy = CategoricalUnivarientAnalyzer()
        df = pd.DataFrame({'test': [1], 'name': ['test1']})
        strategy.setOptions('test').analyse(df)
        self.assertTrue(True)
        mock_figure.assert_called()
        mock_title.assert_called()
        mocl_x_label.assert_called()
        mock_y_label.assert_called()
        mock_show.assert_called()
        mock_sns.assert_called()

if __name__ == '__main__':
    unittest.main()