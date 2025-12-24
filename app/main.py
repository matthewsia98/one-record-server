from contextlib import asynccontextmanager

import pyld.jsonld
from fastapi import (
    FastAPI,
)
from fastapi.middleware.cors import CORSMiddleware

from app.dependencies.http_client import HttpClient
from app.internal import assessment, testing
from app.routers import (
    logistics_events,
    logistics_objects,
    notifications,
    server_information,
    subscriptions,
)

pyld.jsonld.set_document_loader(pyld.jsonld.dummy_document_loader())

http_client = HttpClient()


@asynccontextmanager
async def lifespan(app: FastAPI):
    http_client.start()
    yield
    await http_client.stop()


app = FastAPI(lifespan=lifespan)

app.state.http_client = http_client

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "*",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(server_information.router)
app.include_router(subscriptions.router)
app.include_router(notifications.router)
app.include_router(logistics_objects.router)
app.include_router(logistics_events.router)
app.include_router(assessment.router)
app.include_router(testing.router)
