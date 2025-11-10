from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import os
from database import db

app = FastAPI(title="GenDev IT API", version="1.0.0")

# CORS setup - allow all origins for dev/preview
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "GenDev IT backend up"}


@app.get("/test")
def test():
    try:
        database_url = os.getenv("DATABASE_URL", "not-set")
        database_name = os.getenv("DATABASE_NAME", "not-set")
        connection_status = "connected" if db is not None else "not connected"
        collections: List[str] = []
        if db is not None:
            collections = db.list_collection_names()
        return {
            "backend": "FastAPI",
            "database": "MongoDB",
            "database_url": database_url,
            "database_name": database_name,
            "connection_status": connection_status,
            "collections": collections,
        }
    except Exception as e:
        return {"error": str(e)}
