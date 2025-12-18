from fastapi import (
    FastAPI,
)

from app.internal import assessment, testing
from app.routers import (
    logistics_objects,
    notifications,
    server_information,
    subscriptions,
)

app = FastAPI()

app.include_router(server_information.router)
app.include_router(subscriptions.router)
app.include_router(notifications.router)
app.include_router(logistics_objects.router)
app.include_router(assessment.router)
app.include_router(testing.router)
