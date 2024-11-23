from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.config import config
import firebase_admin
from dotenv import load_dotenv
import pathlib
import uvicorn
import os
from app.routes.userRoutes import router as users_router
from app.routes.healthchekRoutes import router as healthcheck_router
from app.auth.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware
# basedir = pathlib.Path(__file__).parents[1]
# load_dotenv(basedir / ".env")

app = FastAPI()
# firebase_admin.initialize_app()
# main.py
# print("Current App Name:", firebase_admin.get_app().project_id)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Menggunakan PORT dari lingkungan, default 8000
    uvicorn.run(app, host="0.0.0.0", port=port)

@app.get("/", response_class=HTMLResponse)
def root():
    return "<h1>API connection sucessfully</h2>"

app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(healthcheck_router, prefix="/healthcheck", tags=["Healthcheck"])


