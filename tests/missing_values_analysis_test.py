import unittest
import pandas as pd
from unittest.mock import patch
from src.analysis.missing_value_analysis import BasicMissingValueAnalyser

class TestBasicMissingValueAnalyser(unittest.TestCase):

    @patch('builtins.print')
    def test_indeitify_missing_values_with_dataframe(self, mock_print):
        strategy = BasicMissingValueAnalyser()
        df = pd.DataFrame({'test': [1], 'name': ['test1']})
        strategy.indeitify_missing_values(df)
        self.assertTrue(True)
        mock_print.assert_called()

    @patch('src.analysis.missing_value_analysis.plt.figure')
    @patch('src.analysis.missing_value_analysis.plt.title')
    @patch('src.analysis.missing_value_analysis.plt.show')
    @patch('src.analysis.missing_value_analysis.sns.heatmap')
    def test_visualize_missing_values_with_dataframe(self, mock_figure, mock_title, mock_show, mock_sns):
        strategy = BasicMissingValueAnalyser()
        df = pd.DataFrame({'test': [1], 'name': ['test1']})
        strategy.visualize_missing_values(df)
        self.assertTrue(True)
        mock_figure.assert_called()
        mock_title.assert_called()
        mock_show.assert_called()
        mock_sns.assert_called()

if __name__ == '__main__':
    unittest.main()