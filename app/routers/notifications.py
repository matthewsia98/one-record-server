"""
https://iata-cargo.github.io/ONE-Record/stable/API-Security/notifications/
"""

from aiohttp import ClientSession
from devtools import debug
from fastapi import APIRouter, Depends, Response, status

from app.dependencies.graph import parse_graph_as
from app.dependencies.http_client import get_http_client
from app.models.notification import Notification

router = APIRouter()


# https://iata-cargo.github.io/ONE-Record/stable/API-Security/notifications/#send-notification
@router.post(
    "/notifications",
    tags=["notifications"],
    status_code=status.HTTP_204_NO_CONTENT,
    # openapi_extra={
    #     "requestBody": {
    #         "content": {
    #             "application/ld+json": {
    #                 "schema": {"$ref": "#/components/schemas/Notification"},
    #             }
    #         }
    #     }
    # },
    response_class=Response,
    responses={
        204: {"description": "The request has been successful"},
        400: {
            "description": "Notification format is invalid",
            # "content": {
            #     "application/ld+json": {
            #         "schema": {"$ref": "#/components/schemas/Error"},
            #         # "example": {},
            #     }
            # },
        },
        401: {
            "description": "Not authenticated, invalid or expired token",
            # "content": {
            #     "application/ld+json": {
            #         "schema": {"$ref": "#/components/schemas/Error"},
            #         # "example": {},
            #     }
            # },
        },
        403: {
            "description": "Not authorized to perform action",
            # "content": {
            #     "application/ld+json": {
            #         "schema": {"$ref": "#/components/schemas/Error"},
            #         # "example": {},
            #     }
            # },
        },
        404: {
            "description": "Resource Not Found",
            # "content": {
            #     "application/ld+json": {
            #         "schema": {"$ref": "#/components/schemas/Error"},
            #         # "example": {},
            #     }
            # },
        },
        405: {
            "description": "Method not allowed",
            # "content": {
            #     "application/ld+json": {
            #         "schema": {"$ref": "#/components/schemas/Error"},
            #         # "example": {},
            #     }
            # },
        },
        415: {
            "description": "Unsupported content type",
            # "content": {
            #     "application/ld+json": {
            #         "schema": {"$ref": "#/components/schemas/Error"},
            #         # "example": {},
            #     }
            # },
        },
        500: {
            "description": "Internal Server Error",
            # "content": {
            #     "application/ld+json": {
            #         "schema": {"$ref": "#/components/schemas/Error"},
            #         # "example": {},
            #     }
            # },
        },
    },
)
async def receive_notification(
    # accept: str = Header(
    #     alias="Accept",
    #     description="The content type in which the ONE Record client wants the HTTP response formatted.",
    #     example="application/ld+json",
    # ),
    # _doc_body: Notification = Body(...),
    notification: Notification = Depends(parse_graph_as(Notification)),
    http_client: ClientSession = Depends(get_http_client),
):
    debug(notification)

    # Go get the logistics object
    try:
        async with http_client.get(
            str(notification.has_logistics_object),
            params={
                "embedded": "true",
            },
            headers={
                "Accept": "application/ld+json",
            },
        ) as response:
            debug(response.status)
    except Exception as e:
        debug(e)

    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )
