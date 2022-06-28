from fastapi import FastAPI
from pyglottolog import Glottolog
from clldutils.clilib import get_parser_and_subparsers
from pyglottolog import fts
from pyglottolog.cli_util import register_search
from fastapi.encoders import jsonable_encoder

class Args:

    def __init__(self, queryTerm):
        self.repos = glottolog
        self.query = queryTerm

def run_search(args):
    count, results = fts.search_langs(args.repos, args.query)
    return results

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    global glottolog
    glottolog = Glottolog('./glottolog')
    parser, subparsers = get_parser_and_subparsers('glottolog')
    register_search(parser, 'iso:abd')

@app.get("/v1/search/{query}")
async def search_lang(query):
    arg = Args(query)
    results = run_search(arg)

    filtered_results = []

    for result in results:
        json_result = jsonable_encoder(result)
        del json_result["fname"]
        filtered_results.append(json_result)

    return filtered_results

@app.get("/v1/lang/{langid}")
async def read_root(langid):
    lang = glottolog.languoid(langid)
    sources = lang.sources

    if sources:
        del lang.cfg['sources']['glottolog']
        del lang.cfg['sources']

    filtered_family = jsonable_encoder(lang.family)
    del filtered_family["dir"]

    filtered_parent = jsonable_encoder(lang.parent)
    del filtered_parent["dir"]

# TODO: Does not work, why? Memory hog, unresponsive:
#    for src in sources:
#        src = src.get_source(glottolog)
#        print(jsonable_encoder(src))
#        sprint(src.id, color='green')
#        # sprint(src.text())
#        print()

    return {"languoid": langid,
            "names": lang.names,
            "category": lang.category,
            "id": lang.id,
            "glottocode": lang.glottocode,
            "family": filtered_family,
            "parent": filtered_parent,
            "ancestors": lang.ancestors,
            "children": lang.children,
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
