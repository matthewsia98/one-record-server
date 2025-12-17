"""
https://iata-cargo.github.io/ONE-Record/stable/API-Security/notifications/
"""

from devtools import debug
from fastapi import APIRouter, Depends, Header, Response, status

from app.models.notification import Notification

router = APIRouter()


# https://iata-cargo.github.io/ONE-Record/stable/API-Security/notifications/#send-notification
@router.post(
    "/notifications",
    tags=["notifications"],
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
    responses={
        204: {"description": "The request has been successful"},
        400: {
            "description": "Notification format is invalid",
            "content": {
                "application/ld+json": {
                    "schema": {"$ref": "#/components/schemas/Error"},
                    "example": {},
                }
            },
        },
        401: {
            "description": "Not authenticated, invalid or expired token",
            "content": {
                "application/ld+json": {
                    "schema": {"$ref": "#/components/schemas/Error"},
                    "example": {},
                }
            },
        },
        403: {
            "description": "Not authorized to perform action",
            "content": {
                "application/ld+json": {
                    "schema": {"$ref": "#/components/schemas/Error"},
                    "example": {},
                }
            },
        },
        404: {
            "description": "Resource Not Found",
            "content": {
                "application/ld+json": {
                    "schema": {"$ref": "#/components/schemas/Error"},
                    "example": {},
                }
            },
        },
        405: {
            "description": "Method not allowed",
            "content": {
                "application/ld+json": {
                    "schema": {"$ref": "#/components/schemas/Error"},
                    "example": {},
                }
            },
        },
        415: {
            "description": "Unsupported content type",
            "content": {
                "application/ld+json": {
                    "schema": {"$ref": "#/components/schemas/Error"},
                    "example": {},
                }
            },
        },
        500: {
            "description": "Internal Server Error",
            "content": {
                "application/ld+json": {
                    "schema": {"$ref": "#/components/schemas/Error"},
                    "example": {},
                }
            },
        },
    },
)
async def receive_notification(
    accept: str = Header(
        alias="Accept",
        description="The content type in which the ONE Record client wants the HTTP response formatted.",
        example="application/ld+json",
    ),
    notification: Notification = Depends(Notification.from_graph),
):
    debug(notification)

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )
