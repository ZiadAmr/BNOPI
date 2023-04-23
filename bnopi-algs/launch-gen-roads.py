#!/usr/bin/env python3

from os import getenv, system, name

if name == "nt":
    system(
        f'py -3 ../algs/import-roads-from-osm.py {getenv("RADIUS")} {getenv("LATITUDE")} {getenv("LONGITUDE")} -o "{getenv("OUTPUT_FILELOC")}"')
else:
    # otherwise assume we can read the shebang
    system(
        f'../algs/import-roads-from-osm.py {getenv("RADIUS")} {getenv("LATITUDE")} {getenv("LONGITUDE")} -o "{getenv("OUTPUT_FILELOC")}"')
