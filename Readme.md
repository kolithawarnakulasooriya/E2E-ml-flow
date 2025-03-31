
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

**Append New Data Ingestor**

Add new claas as `<type>_data_ingester.py` inherited by the `abs_data_ingester`. Append your code in the `ingest` method and return your ingester object through `data_ingester_factory`.

## Important

If you found an Module not found error, Execute below code

```
import sys
import os
sys.path.append(os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir))))
```