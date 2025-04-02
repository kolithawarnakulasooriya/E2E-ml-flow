
# E2E Machine Learning Framework 

This framework allows an E2E machine learning framework from data ingestion, analysis, and deployments over cloud interfaces.


## Technologies and Frameworks

[![Python](https://img.shields.io/badge/Python-3)](https://www.python.org/about/apps/)



## Framework Components

### Data Ingestors

This component allows you to read data from any file type '.zip' or csv or any.
If your data is in zrchive files, put them in to `/data directory`. We annotated factory design pattern for data ingestor module. 

```
+ src
    |- data_injester
            |- abs_data_ingester.py 
            |- data_ingester_factory.py
            |- zip_data_ingester.py
```

data_ingester_factory allows you to ingest data from your centain datasource.

```
from src.data_ingester.data_ingester_factory import DataIngesterFactory
import pandas as pd

df: pd.Dataframe = DataIngesterFactory.get_data_ingester('.zip').ingest('../data/archive.zip')
```

### Data Analyser

This component allows you to analyse data, such as missing values, variation analysis, etc. This section uses decorator and tempate design patterns to develop components.

1. Data Inspector

```
+ src
    |- analysis
            |- abs_data_inspection_strategy.py  
            |- basic_data_inspection.py
            |- inspection_decorator.py
```

Data inspector uses strategy design pattern which can embed multiple inspectors. inspection_decorator allows yout to run your inspections

```
from src.analysis.basic_data_inspection import DataTypesInspectionStrategy, DataSummaryInspectionStrategy
from src.analysis.inspection_decorator import Inspector

inspecor = Inspector(df)
inspecor.add_strategy(DataTypesInspectionStrategy()).add_strategy(DataSummaryInspectionStrategy()).execute()
```

`abs_data_inspection_strategy.py` provides abstract strategy for the implementations.

2. Missing data analyser

This component allows you to understand and analyse, visualize missing data in the dataset. This component uses templete design pattern to implement analser.

```
+ src
    |- analysis
            |- abs_missing_value_analysis.py  
            |- missing_value_analysis.py
```

`abs_missing_value_analysis.py` provides a abstract interface for missing value analysers. All the analysers are resides in the `missing_value_analysis.py` module.

```
from src.analysis.inspection_decorator import Inspector
from src.analysis.missing_value_analysis import BasicMissingValueAnalyser

analyzer = BasicMissingValueAnalyser()
analyzer.analyse(df)
```

3. Univariant Analyser

This component allows you to understand and analyse, visualize of one feature in the dataset. This component uses strategy design pattern to implement analser.

```
+ src
    |- analysis
            |- abs_variate_analyse_strategy.py  
            |- varient_analysis.py
```

`abs_variate_analyse_strategy.py` provides a abstract interface for all variant analysis. All the analysers are resides in the `varient_analysis.py` module. Here is the exaple for univariant basic neumerical analysis.

```
from src.analysis.varient_analysis import NumericalUnivarientAnalyzer

# Univarient analysers
nva = NumericalUnivarientAnalyzer('city')
nva.analyse(df)
```

3. Bivariant Analyser

This component allows you to understand and analyse, visualize of two features in the dataset. This component uses strategy design pattern to implement analser.

```
from src.analysis.varient_analysis import CategoricalBiVarientAnalysis

# Univarient analysers
nva = CategoricalBiVarientAnalysis('city', 'price')
nva.analyse(df)
```

## Important

If you found an Module not found error, Execute below code

```
import sys
import os
sys.path.append(os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir))))
```