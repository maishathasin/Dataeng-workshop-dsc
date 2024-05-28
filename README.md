# Dataeng-workshop-dsc



![Airflow](https://img.shields.io/badge/apache-airflow-017CEE.svg?logo=apache-airflow)
![Spark](https://img.shields.io/badge/apache-spark-E25A1C.svg?logo=apachespark)

This guide will help you set up Apache Airflow and Apache Spark for the Data Engineering workshop.

## Prerequisites

Ensure you have the following installed:
- Python 3.7+


## Clone this repo 

```
git clone https://github.com/maishathasin/Dataeng-workshop-dsc.git

```

## Setting Up Apache Airflow

### Install Apache Airflow

```bash
pip install apache-airflow
```

### Initialize the Airflow Database
```bash
airflow db init
```

### Configure Airflow Home Directory to your current directory
```bash
export AIRFLOW_HOME= .
source ~/.bashrc  # or source ~/.zshrc
```


### Place Your DAG File
Place your data_ingestion_dag.py file in the /dags directory. Verify the file is there:

```bash
airflow/
    ├── dags/
    │   ├── data_ingestion_dag.py
    ├── logs/
    ├── plugins/
    └── airflow.cfg


```


### Update Airflow Configuration

```python

[core]
airflow_home = /path/to/airflow

dags_folder = /path/to/airflow/dags

```


### Start airflow 

In two different terminals, run the following commands:


```bash
airflow webserver --port 8080
```

```bash
airflow scheduler
```


## Installing PySpark 

 To install PySpark on Windows follow this: https://www.machinelearningplus.com/pyspark/install-pyspark-on-windows/
 To install PySpark on Mac follow this: https://www.machinelearningplus.com/pyspark/install-pyspark-on-mac/

 Other systems:
 https://www.datacamp.com/tutorial/installation-of-pyspark (This has Mac, Windows and Linux instructions)




## Contrbutions 

If you find any problems, please make a pull request or an issue !