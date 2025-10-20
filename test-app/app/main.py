from fastapi import FastAPI
import os


app = FastAPI()


@app.get("/")
def read_root():
    # show we can read envs loaded via --env-file
    return {"message": "Hello from FastAPI in Docker!", "env_sample": os.getenv("APP_NAME", "unset")}
