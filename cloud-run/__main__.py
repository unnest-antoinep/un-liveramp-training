import uvicorn

from main import app


def start_app():
    uvicorn.run(app, host="0.0.0.0", port=8080)


start_app()