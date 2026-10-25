from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="enterprise-rag")


class HealthResponse(BaseModel):
    status: str


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    """Liveness check: confirms the API process is up."""
    return HealthResponse(status="ok")
