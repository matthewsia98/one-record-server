import requests
from rdflib import Graph, OWL, RDF
from _API import API


response = requests.get("https://onerecord.iata.org/ns/api/ontology.ttl")
g = Graph()
g.parse(data=response.content)


for s in g.subjects(RDF.type, OWL.Class):
    print(s)
    if s == API.AccessDelegation:
        print(s)
        for p, o in g.predicate_objects(s):
            print(f"  {p} {o}")
