
# Dependency Graphs

## Backend Node Structure
A JSON object containing the following properties:

+ `id: String` - the ID of the node as referred to elsewhere int he project
+ `name: String` - the name of the stage as set in the frontend of the project
+ `params: JSON` - the JSON object containing the name and value of the parameters as set in the metadata file. This will be described in detail later in this file
+ `parents: Array[String]` - list containing the ID of the parent node(s) of this node
+ `description: String` - the description as set in the frontend and metadata files
+ `input_stage_format: JSON` - JSON object containing information about the input stages to this stage, contains the unique identifer of the stage. Will be explained in detail later
+ `output_stage_format: JSON` - JSON object containing information about the output stages to this stage, contains the unique identifer of the stage. Will be explained in detail later

### params Object Structure
+ `choices: Array[String]` - Optional, contains the possible options if the param can only have predefined options
+ `default: String` - contains the default value if none is assigned
+ `help: String` - Defined in metadata file
+ `setVal: String` - The value set for the parameter in the front-end
+ `type: String` - The type of the value, for example dropdown or posint
+ `var: String` - The name of the environment variable associated with the parameter, set in the metadata file

### Stage Format Object Structure
+ `help: String` - A string set in the metadata
+ `name: String` - Name assigned to the stage
+ `setStage: String` - The file containing the stage, used as a unique identifer for the stage
+ `var: String` - The name of the environment variable associated with the stage, set in the metadata file