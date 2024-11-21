from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.config import config


from app.routes.userRoutes import router as users_router
from app.routes.healthchekRoutes import router as healthcheck_router

app = FastAPI()

# main.py

print(config)

@app.get("/", response_class=HTMLResponse)
def healthcheck():
    return "<h1>API connection sucessfully</h2>"

app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(healthcheck_router, prefix="/healthcheck", tags=["Healthcheck"])


