![GitHub](https://img.shields.io/github/license/gesteves91/replication-package-unified%20)

# Replication Package Unified

## Overview
-------

This replication package outlines the data transformation procedures employed for the unified dataset.

### Data

All data is available under the [data](https://github.com/anonymous-replication/replication-package-unified/tree/main/data) folder. The list of data sources is as follows:

- Unified-class.csv
- unified-cleaned.csv
- unified-processed.csv
- unified-processed.csv

Example file paths:

```bash
./data/Unified-class.csv
./data/unified-cleaned.csv
./data/unified-processed.csv
./data/unified-explored.csv
```

#### Features

The comprehensive list of data features applied in this dataset can be found [here](https://github.com/anonymous-replication/replication-package-unified/blob/main/features/features.md).

### Data Preparation

The replication package includes the following data preparation steps:

#### Data Cleaning

- [x] Removal of duplicate entries
- [x] Handling of missing values
- [x] Conversion of non-numeric data to numeric

#### Data Exploration

- [x] Normalization using Standard Scaler
- [x] Balancing via SMOTE
- [x] Encoding with One-Hot

#### Feature Engineering

- [x] Feature Selection
- [x] Correlation Analysis
- [x] Variance Analysis

### Requirements

To replicate these data transformations, please ensure you have the necessary dependencies installed. All requirements can be found in the **requirements.txt** file. We recommend using Python 3 Virtual Environment:

```
pip3 install -r requirements.txt
```

### Interpretability

To gain insights and interpret the dataset, execute the primary notebook located in the notebooks directory.

Example notebook path:

```bash
./notebooks/02-shap.ipynb
```
