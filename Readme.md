## How to use 

first create a virtual env and activate it 

```
python -m venv .venv
source .venv/bin/activate
```

intall the dependencies for the cloud function and the cloud run

```
pip install -r ./cloud-function/requirements.txt
pip install -r ./cloud-run/requirements.txt
```


## Deploy the cloud function

```
gcloud builds submit --region=europe-west1 --config ./cloud-function/cloudbuild.yaml ./cloud-function
```

## Test cloud run locally

In the cloud run directory build the docker image

```
docker build -t test . 
```

Run it and navigate to localhost:8080

```
docker run -p 127.0.0.1:8080:8080 -v ~/.config/gcloud:/root/.config/gcloud test
```

## Deploy the cloud run

```
gcloud builds submit --region=europe-west1 --config ./cloud-run/cloudbuild.yaml ./cloud-function
```