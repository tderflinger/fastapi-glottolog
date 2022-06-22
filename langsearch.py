"""
Search Glottolog languoids.

Note: The search index will be created upon first invocation of this command.
"""
from pyglottolog import fts
from pyglottolog.cli_util import register_search


def register(parser):
    register_search(parser, 'iso:abd')

def run(args):
    count, results = fts.search_langs(args.repos, args.query)
    return results
