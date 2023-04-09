# Algorithms

The folder [/bnopi-algs/](/bnopi-algs/) contains metadata about algorithms required by BNOPI. For each algorithm there is an *.alg.json* file. For each project BNOPI will be able to access algorithms referenced in /bnopi-algs/ and (NOT IMPLEMENTED) in a folder inside the project directory.

## Procedure for running an algorithm

When an algorithm has been assigned to a node, the user can edit the algorithm **parameters** from the *properties* tab in the sidebar. These can be used as input to the algorithm in addition to stage instances, for example to set some command line arguments for the algorithm. The *.alg.json* file contains a `"params"` array, specifying what parameters are needed for the algorithm.

<!-- param type definition  -->

<!-- procedure for selecting stage instance dependencies (NOT IMPLEMENTED) -->

The input stage formats are defined in the *.alg.json* file in the `"input-stage-formats"` property. When the algorithm is assigned to a node in the dependency graph, in order to run the node there must be one incoming edge for each of these input stage formats.

<!-- stage format type definition -->

When the algorithm is to start running, BNOPI allocates a new file name for each output stage instance. It then exports each parameter value and stage format path as an environment variable (the name of which is specified by `var`) and runs one of the launch shell scripts specified in the `"launch-script"` property. This script will do any necessary preprocessing and then call the algorithm.


## *.alg.js* structure

<!-- TODO -->



