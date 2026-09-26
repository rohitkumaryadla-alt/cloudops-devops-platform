from fastapi import FastAPI

from app.database import Base, engine

import app.models

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CloudOps API",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/")
def root():
    return {
        "message": "CloudOps API is running"
    }