from typing import Optional

from aiohttp import ClientSession
from fastapi import Request


class HttpClient:
    session: Optional[ClientSession] = None

    def start(self):
        self.session = ClientSession()

    async def stop(self):
        await self.session.close()
        self.session = None

    def __call__(self) -> ClientSession:
        assert self.session is not None
        return self.session


def get_http_client(request: Request) -> ClientSession:
    return request.app.state.http_client()
