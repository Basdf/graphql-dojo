from fastapi import FastAPI

from app.core.db import Base, engine
from app.core.debugger import initialize_fastapi_server_debugger_if_needed
from app.core.logging import get_logger
from app.infra.strawberry.query import graphql_app

log = get_logger(__name__)

initialize_fastapi_server_debugger_if_needed()
app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    # create db tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
