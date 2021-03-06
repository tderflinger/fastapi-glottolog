# fastapi-glottolog

[![License:MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

REST API for [Glottolog](https://glottolog.org/) using Python FastAPI.

Note: This is a project independent of Glottolog.org.

## Installation

python3 -m venv venv

. venv/bin/activate

pip3 install -r requirements.txt

Clone Glottolog into ./app folder: 

```bash
cd app
git clone https://github.com/glottolog/glottolog
```

## Run for Development

```bash
cd app
uvicorn main:app --reload
```

Try searching by language e.g.:

http://localhost:8000/v1/search/Indonesian

Try searching by Glottolog id:

http://localhost:8000/v1/lang/pera1256

## OpenAPI Documentation

Run `uvicorn main:app --reload` and open http://localhost:8000/docs/

## Docker

Create the Docker image with:

```bash
docker build -t fastapi-glottolog .
```

Run with:

```bash
docker run -d --name fastapi-glottolog-container -p 80:80 fastapi-glottolog
```

Log in to Container:

```bash
docker exec -it -u root fastapi-glottolog-container /bin/bash
```

Pre-built Image in Docker Hub:

https://hub.docker.com/r/tderflinger/fastapi-glottolog

Pull Image:

```bash
docker pull tderflinger/fastapi-glottolog:0.1.0
```

## Roadmap

- Return bibliographical information for languages.
- CLI for API

## References

Glottolog: https://glottolog.org/

pyglottolog: https://github.com/glottolog/pyglottolog

FastAPI:  https://fastapi.tiangolo.com/

## License

Fastapi-glottolog is licensed under the MIT License

The Glottolog data is licensed as CC-BY 4.0: https://creativecommons.org/licenses/by/4.0/
