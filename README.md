# ONE Record Server

<https://iata-cargo.github.io/ONE-Record/stable/>

## Quick Start

### Run Development Server

```
uv run fastapi dev app/main.py
```

### Create Dev Virtual Environment

```
uv sync --dev
```

### Type Checking

```
uv run mypy <path>
```

### Formatting

```
uvx format
```

### Linting

```
uvx check
```

```
uvx check --fix
```

### Git Hooks

```
uv run pre-commit install
```

```
uv run pre-commit run --all-files
```

## Docker

### Build image

```
docker build -t one-record-server .
```

### Create and run container

```
docker run -p 8000:8000 one-record-server
```

### Start existing container

```
docker start -d -p 8000:8000 --name one-record-server one-record-server
```

## Generate Namespace Bindings

```
uv run generate_namespaces.py
```

## Resources

| Name                                | Link                                                                             |
| ----------------------------------- | -------------------------------------------------------------------------------- |
| API Specification                   | <https://iata-cargo.github.io/ONE-Record/stable/API-Security/>                     |
| PLACI                               | <https://iata-cargo.github.io/ONE-Record/stable/Orchestration/placi/>              |
| CXML Mapping                        | <https://iata-cargo.github.io/ONE-Record/stable/Orchestration/orchestration-cxml/> |
| Cargo Ontology                      | <https://onerecord.iata.org/ns/cargo/index-en.html>                                |
| API Ontology                        | <https://onerecord.iata.org/ns/api/index-en.html>                                  |
| Code Lists Ontology                 | <https://onerecord.iata.org/ns/code-lists/index-en.html>                           |
| ONE Record Implmentation            | <https://git.openlogisticsfoundation.org/wg-digitalaircargo/ne-one>                |
| (Archived) ONE Record Implmentation | <https://github.com/IATA-Cargo/one-record-server-java>                             |
| ONE Record Demonstrator             | <https://github.com/IATA-Cargo/one-record-demonstrator>                            |
| Ontology Visualizer                 | <https://iata-cargo.github.io/ontology_visualizer/databases/cargo_3_2>             |
