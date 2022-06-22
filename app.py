from fastapi import FastAPI
from pyglottolog import Glottolog
from clldutils.clilib import get_parser_and_subparsers
import uvicorn
import langsearch

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    global glottolog
    glottolog = Glottolog('./glottolog')
    parser, subparsers = get_parser_and_subparsers('glottolog')
    langsearch.register(parser)

class Args:

    def __init__(self, queryTerm):
        self.repos = glottolog
        self.query = queryTerm

@app.get("/search/{query}")
async def search_lang(query):
    arg = Args(query)
    results = langsearch.run(arg)

    return results

@app.get("/lang/{langid}")
async def read_root(langid):
    lang = glottolog.languoid(langid)
    sources = lang.sources

    if sources:
        del lang.cfg['sources']['glottolog']
        del lang.cfg['sources']

# TODO: Does not work, why? Memory hog, unresponsive:
#    for src in sources:
#        src = src.get_source(glottolog)
#        sprint(src.id, color='green')
#        # sprint(src.text())
#        print()

    return {"languoid": langid,
            "names": lang.names,
            "category": lang.category,
            "id": lang.id,
            "glottocode": lang.glottocode,
            "family": lang.family,
            "parent": lang.parent,
            "ancestors": lang.ancestors,
            "children": lang.children,
            "path": lang.fname,
            "identifier": lang.identifier,
            "endangerment": lang.endangerment,
            "classification_comment": lang.classification_comment,
            "ethnologue_comment": lang.ethnologue_comment,
            "macroareas": lang.macroareas,
            "timespan": lang.timespan,
            "links": lang.links,
            "countries": lang.countries,
            "name": lang.name,
            "latitude": lang.latitude,
            "longitude": lang.longitude,
            "hid": lang.hid,
            "level": lang.level,
            "iso": lang.iso,
            "iso_code": lang.iso_code,
            "isolate": lang.isolate}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host="0.0.0.0")
