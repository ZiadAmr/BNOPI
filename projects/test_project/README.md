# Test project
This project shows how projects will be saved.

## Files in this folder

### info.json
All projects have this file. This is the only file with a fixed name; everything else is linked within it.

### Dependency graph file (*.dg.json)
Users are able to open these within the editor. The info.json file contains the currently selected dg file for the project.

### Stage instance folder
`info.json` contains a list of folders within which BNOPI looks for stage instance metadata files (with the extension `*.stg.json`).

### Stage instance metadata file (*.stg.json)
[stage_instances/STOPS_1.stg.json](stage_instances/STOPS_1.stg.json) is a stage instance metadata file. It contains metadata and a link to the actual stage instance.

### Stage instance
[stage_instances/broughton_stops.json](stage_instances/broughton_stops.json) is the stage instance pointed to by the stage instance metadata file [stage_instances/STOPS_1.stg.json](stage_instances/STOPS_1.stg.json).

## Files elsewhere

### Stage formats
These are referenced using their IDs, such as `STOPS`. These must be added from API calls, rather than BNOPI searching folders. An example is shown at [/bnopi-stage-fmts/stops-format.js](/bnopi-stage-fmts/stops-format.js).

### Algorithms
Referenced by the dependency graph. See [/bnopi-algs/](/bnopi-algs/)

