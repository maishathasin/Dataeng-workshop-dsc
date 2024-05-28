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


## Setting Up a Virtual Environment

Creating a virtual environment is a good practice to manage dependencies and avoid conflicts.

### Create a Virtual Environment

```bash
python3 -m venv airflow-env
```

### Activate the Virtual Environment

On macOS and Linux:

```bash
source airflow-env/bin/activate
```

On Windows:

```bash
airflow-env\Scripts\activate
```


Once the virtual environment is activated, you can proceed to install Apache Airflow and other dependencies.


## Setting Up Apache Airflow

### Install Apache Airflow

```bash
pip install apache-airflow
```

### Configure Airflow Home Directory to your current directory
```bash
export AIRFLOW_HOME= . # its better to use ~airflow and save it in your home 
source ~/.bashrc  # or source ~/.zshrc
```
### Initialize the Airflow Database
```bash
airflow db init

airflow users create --username admin --password admin --firstname Admin --lastname User --role Admin --email admin@example.com

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

 To install PySpark on Windows follow this: 
 
 https://www.machinelearningplus.com/pyspark/install-pyspark-on-windows/


 To install PySpark on Mac follow this:
 
  https://www.machinelearningplus.com/pyspark/install-pyspark-on-mac/

 Other systems:

 https://www.datacamp.com/tutorial/installation-of-pyspark (This has Mac, Windows and Linux instructions)




## Contrbutions 

If you find any problems, please make a pull request or an issue !