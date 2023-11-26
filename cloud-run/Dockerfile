FROM python:3.11.6-slim-bookworm

ENV APP_PATH=/usr/src/api
ENV PORT=8080

RUN mkdir -p $APP_PATH

COPY . $APP_PATH

WORKDIR $APP_PATH

RUN pip install -r requirements.txt

EXPOSE $PORT

# Use uvicorn as the entrypoint
ENTRYPOINT [ "/bin/bash", "-c", "uvicorn api.main:app --host 0.0.0.0 --port ${PORT}"]
