# One Record Server

## uv

```
uv run fastapi dev app/main.py
```

```
uv sync --dev
```

```
uv run mypy <path>
```

```
uvx format
```

```
uvx check
```

```
uvx check --fix
```

```
uv run pre-commit install
```

```
uv run pre-commit run --all-files
```

## Docker

```
docker build -t one-record-server .
```

```
docker run -p 8000:80 one-record-server
```

```
docker start -d -p 8000:8000 --name one-record-server one-record-server
```

## Generate Namespace Bindings

```
uv run python -m rdflib.tools.defined_namespace_creator https://onerecord.iata.org/ns/api/ontology.ttl https://onerecord.iata.org/ns/api# API

uv run python -m rdflib.tools.defined_namespace_creator https://onerecord.iata.org/ns/cargo/ontology.ttl https://onerecord.iata.org/ns/cargo# CARGO
```
