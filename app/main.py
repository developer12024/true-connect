from fastapi import FastAPI
from app.api.v1 import profiles
from app.db import init_db

app = FastAPI(title="true-connect")

app.include_router(profiles.router)

@app.on_event("startup")
async def on_startup():
    # initialize tables in dev (production: use alembic)
    await init_db()