from fastapi import FastAPI

from app.api.routes.health import router as health_router
from app.core.config import settings
from app.core.logging import setup_logging, logger

setup_logging()

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Self-Service Cloud Infrastructure and DevOps Platform",
    version=settings.PROJECT_VERSION,
    debug=settings.DEBUG
)

app.include_router(health_router)


@app.on_event("startup")
def startup_event():
    logger.info("%s API started", settings.PROJECT_NAME)


@app.get("/")
def root():
    logger.info("Root endpoint accessed")

    return {
        "project": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
        "environment": settings.ENVIRONMENT,
        "status": "running",
        "message": "Welcome to CloudPilot Platform"
    }
