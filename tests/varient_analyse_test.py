import unittest
import pandas as pd
from unittest.mock import patch
from src.analysis.varient_analysis import NumericalUnivarientAnalyzer, \
    CategoricalUnivarientAnalyzer, NumericalBiVarientAnalysis, CategoricalBiVarientAnalysis, BasicMultiVarientAnalysis

class TestNumericalUnivarientAnalyzer(unittest.TestCase):

    @patch('src.analysis.varient_analysis.plt.figure')
    @patch('src.analysis.varient_analysis.plt.title')
    @patch('src.analysis.varient_analysis.plt.xlabel')
    @patch('src.analysis.varient_analysis.plt.ylabel')
    @patch('src.analysis.varient_analysis.plt.show')
    @patch('src.analysis.varient_analysis.histplot')
    def test_analyse(self, mock_figure, mock_title, mocl_x_label, mock_y_label, mock_show, mock_sns):
        strategy = NumericalUnivarientAnalyzer('test')
        df = pd.DataFrame({'test': [1], 'name': ['test1']})
        strategy.analyse(df)
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
        strategy = CategoricalUnivarientAnalyzer('test')
        df = pd.DataFrame({'test': [1], 'name': ['test1']})
        strategy.analyse(df)
        self.assertTrue(True)
        mock_figure.assert_called()
        mock_title.assert_called()
        mocl_x_label.assert_called()
        mock_y_label.assert_called()
        mock_show.assert_called()
        mock_sns.assert_called()

class TestNumericalBiVarientAnalysis(unittest.TestCase):

    @patch('src.analysis.varient_analysis.plt.figure')
    @patch('src.analysis.varient_analysis.plt.title')
    @patch('src.analysis.varient_analysis.plt.xlabel')
    @patch('src.analysis.varient_analysis.plt.ylabel')
    @patch('src.analysis.varient_analysis.plt.show')
    @patch('src.analysis.varient_analysis.scatterplot')
    def test_analyse(self, mock_figure, mock_title, mocl_x_label, mock_y_label, mock_show, mock_sns):
        strategy = NumericalBiVarientAnalysis('test', 'name')
        df = pd.DataFrame({'test': [1], 'name': ['test1']})
        strategy.analyse(df)
        self.assertTrue(True)
        mock_figure.assert_called()
        mock_title.assert_called()
        mocl_x_label.assert_called()
        mock_y_label.assert_called()
        mock_show.assert_called()
        mock_sns.assert_called()

class TestCategoricalBiVarientAnalysis(unittest.TestCase):

    @patch('src.analysis.varient_analysis.plt.figure')
    @patch('src.analysis.varient_analysis.plt.title')
    @patch('src.analysis.varient_analysis.plt.xlabel')
    @patch('src.analysis.varient_analysis.plt.ylabel')
    @patch('src.analysis.varient_analysis.plt.show')
    @patch('src.analysis.varient_analysis.boxplot')
    def test_analyse(self, mock_figure, mock_title, mocl_x_label, mock_y_label, mock_show, mock_sns):
        strategy = CategoricalBiVarientAnalysis('test', 'name')
        df = pd.DataFrame({'test': [1], 'name': ['test1']})
        strategy.analyse(df)
        self.assertTrue(True)
        mock_figure.assert_called()
        mock_title.assert_called()
        mocl_x_label.assert_called()
        mock_y_label.assert_called()
        mock_show.assert_called()
        mock_sns.assert_called()

class TestBasicMultiVarientAnalysis(unittest.TestCase):

    @patch('src.analysis.varient_analysis.plt.figure')
    @patch('src.analysis.varient_analysis.plt.title')
    @patch('src.analysis.varient_analysis.plt.show')
    @patch('src.analysis.varient_analysis.heatmap')
    def test_generate_corr_heatmap(self, mock_figure, mock_title, mock_show, mock_sns):
        strategy = BasicMultiVarientAnalysis()
        df = pd.DataFrame({'test1': [1], 'test2': [2]})
        strategy.generate_corr_heatmap(df)
        self.assertTrue(True)
        mock_figure.assert_called()
        mock_title.assert_called()
        mock_show.assert_called()
        mock_sns.assert_called()

    @patch('src.analysis.varient_analysis.plt.figure')
    @patch('src.analysis.varient_analysis.plt.title')
    @patch('src.analysis.varient_analysis.plt.show')
    @patch('src.analysis.varient_analysis.heatmap')
    @patch('src.analysis.varient_analysis.pairplot')
    def test_generate_corr_heatmap(self, mock_figure, mock_title, mock_show, mock_sns_heatmap, mock_sns_pairplot):
        strategy = BasicMultiVarientAnalysis()
        df = pd.DataFrame({'test1': [1], 'test2': [2]})
        strategy.analyse(df)
        self.assertTrue(True)
        mock_figure.assert_called()
        mock_title.assert_called()
        mock_show.assert_called()
        mock_sns_heatmap.assert_called()
        mock_sns_pairplot.assert_called()

    @patch('src.analysis.varient_analysis.plt.figure')
    @patch('src.analysis.varient_analysis.plt.title')
    @patch('src.analysis.varient_analysis.plt.show')
    @patch('src.analysis.varient_analysis.pairplot')
    def test_analysis(self, mock_figure, mock_title, mock_show, mock_sns):
        strategy = BasicMultiVarientAnalysis()
        df = pd.DataFrame({'test1': [1], 'test2': [2]})
        strategy.generate_pairplot(df)
        self.assertTrue(True)
        mock_figure.assert_called()
        mock_title.assert_called()
        mock_show.assert_called()
        mock_sns.assert_called()



if __name__ == '__main__':
    unittest.main()