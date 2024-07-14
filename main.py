import uvicorn
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from dashapp import app as app_dash

app = FastAPI()
# Mount the Dash app as a sub-application in the FastAPI server
app.mount("/dashboard1", WSGIMiddleware(app_dash.server))


@app.get("/")
def index():
    return "Hello, I'm working this is a test endpoint"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0")
