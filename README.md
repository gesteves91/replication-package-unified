# Replication Package Unified

SUMMARY
-------

This replication package describes the data transformation used in the unified dataset.

### Data

All data is available under the [data](https://github.com/anonymous-replication/replication-package-unified/tree/main/data) folder. The list of data sources are presented below:

- Unified-class.csv
- unified-cleaned.csv
- unified-processed.csv
- unified-processed.csv

Example:

```bash
./data/Unified-class.csv
./data/unified-cleaned.csv
./data/unified-processed.csv
./data/unified-explored.csv
```

#### Features

The complete list of features applied in the data is available [here](https://github.com/anonymous-replication/replication-package-unified/blob/main/features/features.md).

### Data Preparation

Next, we show the data preparation steps executed in the replication package.

#### Data Cleaning

- [x] Remove duplicate entries
- [x] Missing values
- [x] Non-numeric data

#### Data Exploration

- [x] Normalization (Standard Scaler)
- [x] Balancing (SMOTE)
- [x] Encoding (One-Hot)

#### Feature Engineering

- [x] Feature Selection
- [x] Correlation Analysis
- [x] Variance Analysis

### Requirements 

All the requirements to apply the data are available under the **requirements.txt**

We recommend using Python 3 Virtual Environment

```
pip3 install -r requirements.txt
```
### Interpretability

Execute the main notebook stored in the **notebook** folder.

Example:

```bash
./notebooks/shap.ipynb
```

