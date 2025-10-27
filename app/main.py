from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.db.session import engine
from app.db.base import Base

# Import models to load metadata before create_all
from app.models import user  # noqa

from app.routers import auth

app = FastAPI(
    title="MediaHub API",
    version="0.1.0",
    docs_url="/docs",
    openapi_url="/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

# MVP: create tables automatically (migrations can be added later)
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)

@app.get("/", tags=["Health"])
def health():
    return {"status": "ok", "env": settings.APP_ENV}
