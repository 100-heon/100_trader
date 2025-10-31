from typing import Optional

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

from . import data_access

app = FastAPI(title="AI-Trader Dashboard API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/api/summary")
def api_summary():
    return data_access.repo_summary()


@app.get("/api/signatures")
def api_signatures():
    return {"signatures": data_access.list_signatures()}


@app.get("/api/positions/{signature}")
def api_positions(signature: str, limit: Optional[int] = Query(default=100, ge=1, le=5000)):
    records = data_access.read_positions(signature, limit=limit)
    if not records:
        raise HTTPException(status_code=404, detail=f"No position data for signature '{signature}'")
    return {"signature": signature, "count": len(records), "records": records}


@app.get("/api/positions/{signature}/latest")
def api_latest_position(signature: str):
    record = data_access.latest_position(signature)
    if not record:
        raise HTTPException(status_code=404, detail=f"No position data for signature '{signature}'")
    return record


@app.get("/api/metrics/{signature}")
def api_metrics(signature: str, limit: Optional[int] = Query(default=50, ge=1, le=1000)):
    records = data_access.read_metrics(signature, limit=limit)
    if not records:
        raise HTTPException(status_code=404, detail=f"No metrics data for signature '{signature}'")
    return {"signature": signature, "count": len(records), "records": records}


@app.get("/api/metrics/{signature}/latest")
def api_latest_metrics(signature: str):
    record = data_access.latest_metrics(signature)
    if not record:
        raise HTTPException(status_code=404, detail=f"No metrics data for signature '{signature}'")
    return record
