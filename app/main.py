from fastapi import (
    FastAPI,
)

from app.routers import subscriptions, notifications
from app.internal import testing


app = FastAPI()
app.include_router(subscriptions.router)
app.include_router(notifications.router)
app.include_router(testing.router)
