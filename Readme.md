## Deploy the cloud function

```
gcloud builds submit --region=europe-west1 --config ./cloud-function/cloudbuild.yaml ./cloud-function
```