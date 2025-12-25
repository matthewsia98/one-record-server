from fastapi.testclient import TestClient
from rdflib import Graph

from app.models.server_information import ServerInformation


def test_get_server_information(client: TestClient):
    response = client.get("/")
    print(response.json())
    g = Graph()
    g.parse(data=response.content, format="json-ld")
    server_information = ServerInformation.from_graph(g)
    print(server_information)
