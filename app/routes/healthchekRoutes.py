from fastapi import APIRouter
from app.handlers.healthcheckHandlers import healthcheck

router = APIRouter()

@router.get("/")
async def healthcheck_route():
    return await healthcheck()
