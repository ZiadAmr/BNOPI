#!/usr/bin/env python3

from os import getenv, system, name

if name == "nt":
    system(
        f'py -3 ../algs/import-stops-from-osm.py {getenv("WORK_AREA_RADIUS")} {getenv("WORK_AREA_LAT")} {getenv("WORK_AREA_LON")} -o "{getenv("OUTPUT_FILELOC")}"')
else:
    # otherwise assume we can read the shebang
    system(
        f'../algs/import-stops-from-osm.py {getenv("WORK_AREA_RADIUS")} {getenv("WORK_AREA_LAT")} {getenv("WORK_AREA_LON")} -o "{getenv("OUTPUT_FILELOC")}"')

