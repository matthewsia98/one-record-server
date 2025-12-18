from fastapi import (
    FastAPI,
)

from app.internal import testing
from app.routers import logistics_objects, notifications, subscriptions

app = FastAPI()

app.include_router(subscriptions.router)
app.include_router(notifications.router)
app.include_router(logistics_objects.router)
app.include_router(testing.router)
