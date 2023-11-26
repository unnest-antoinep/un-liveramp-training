from fastapi import FastAPI
import requests
import pandas as pd
from google.cloud import bigquery

app = FastAPI()

PROJECT_ID = 'un-liveramp-training'
DATASET_ID = 'liveramp_training'
TABLE_ID = 'fruits'

def clean_columns(df):
    df.columns = df.columns.str.replace(r'(', '')
    df.columns = df.columns.str.replace(r')', '')
    df.columns = df.columns.str.replace(r'[', '')
    df.columns = df.columns.str.replace(r']', '')
    df.columns = df.columns.str.replace('.', '_')
    return df.columns.str.replace(' ', '_')

@app.get("/")
def main(request):

    _ = request.get_json(silent=True)
    _ = request.args

    req = requests.get('https://www.fruityvice.com/api/fruit/all')
    df = pd.json_normalize(req.json())
    df.head()

    client = bigquery.Client(project=PROJECT_ID)
    dataset = client.dataset(DATASET_ID)
    table = dataset.table(TABLE_ID)

    job_config = bigquery.LoadJobConfig()
    job_config.autodetect = True
    job_config.write_disposition = "WRITE_APPEND"
    job_config.create_disposition = "CREATE_IF_NEEDED"

    df.columns = clean_columns(df)

    job = client.load_table_from_dataframe(
        df, table, job_config=job_config
        )  
    job.result()

    return 'ok'
