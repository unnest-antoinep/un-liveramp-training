from fastapi import FastAPI
import requests
import pandas as pd
from google.cloud import bigquery
import google.auth


app = FastAPI()

PROJECT_ID = 'un-liveramp-training'
DATASET_ID = 'liveramp_training'
TABLE_ID = 'fruits_cloudrun'

def clean_columns(df):
    df.columns = df.columns.str.replace(r'(', '')
    df.columns = df.columns.str.replace(r')', '')
    df.columns = df.columns.str.replace(r'[', '')
    df.columns = df.columns.str.replace(r']', '')
    df.columns = df.columns.str.replace('.', '_')
    return df.columns.str.replace(' ', '_')

@app.get("/")
def main():

    credentials, project = google.auth.default()

    req = requests.get('https://www.fruityvice.com/api/fruit/all')
    df = pd.json_normalize(req.json())
    df.head()

    client = bigquery.Client(project=PROJECT_ID, location='EU')
    dataset = client.dataset(DATASET_ID)
    table = dataset.table(TABLE_ID)

    job_config = bigquery.LoadJobConfig()
    job_config.autodetect = True
    job_config.create_disposition = "CREATE_IF_NEEDED"

    df.columns = clean_columns(df)

    job = client.load_table_from_dataframe(
        df, table, job_config=job_config
        )  
    job.result()

    return 'ok'
