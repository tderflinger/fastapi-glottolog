# fastapi-glottolog

REST API for [Glottolog](https://glottolog.org/) using Python Fastapi.

## Installation

python3 -m venv venv

. venv/bin/activate

pip3 install -r requirements.txt

Clone Glottolog into root folder: https://github.com/glottolog/glottolog

## Run for Development

```bash
python3 app.py
```

Try searching language e.g.:

http://localhost:8080/search/Indonesian

Try searching by Glottolog id:

http://localhost:8080/lang/pera1256

## Run for Production

With reloading:

```bash
uvicorn app:app --reload
```

## API Documentation:

Run `uvicorn app:app --reload` and open http://localhost:8000/docs/

## References

Glottolog: https://glottolog.org/

pyglottolog: https://github.com/glottolog/pyglottolog

FastAPI:  https://fastapi.tiangolo.com/

## License

MIT License
