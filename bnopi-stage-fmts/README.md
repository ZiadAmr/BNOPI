# Stage Formats

In this document stage instances will sometimes be refered to as just "instances", and likewise with stage formats being referred to as "formats".

## Procedure for displaying a stage instance

The stage tracker displays a list of [*.stg.json* files](/projects/test_project/) which contains some metadata and point to the actual stage instance. The user selects an item from this list, which will be referred to as the **primary instance**.

BNOPI then reads the *.stg.json* file of the selected primary instance. It contains the `format` property, which is the instance's stage format. It then tries to identify the stage format. If there is a *.fmt.js* for this stage in the directory [/bnopi-stage-fmts/](/bnopi-stage-fmts/), then this will have been loaded when BNOPI is opened.

NOT IMPLEMENTED: In the future, projects will be able to add their own *.fmt.js* files.

In some cases, opening a stage format has some extra **requirements**; these are other stage instances that are needed in combination with the primary stage instance in order to display useful information of the map. For example, displaying a ROUTE_NETWORK instance requires access to a STOP_CONNECTION_GRAPH instance, as the route network references edges in the stop connection graph. If there are requirements, the user will be prompted to select the requirement stage instances (BNOPI can guess these from the dependency graph also).

BNOPI then reads the primary instance (referenced in the *.stg.json* file) and the requirement instances into `Buffer` objects. It calls the **display framework** of the stage format, defined in the *.fmt.js*.

```typescript
(method) displayFramework(primaryInstance: BNOPIInstance, requirementInstances: BNOPIInstance[], stageFormatHandler: StageFormatHandler): {
	stops: BNOPIStop[];
	routes: BNOPIRoute[];
}
```
<!-- which is of the form

	displayFramework(primaryInstance: BNOPIInstance, requirementInstances: BNOPIInstance[], stageFormatHandler: StageFormatHandler): {
		stops: BNOPIStop[];
		routes: BNOPIRoute[];
	}

`Stop` is typed as
```
Stop: {
	lat: float,
	lon: float,
	id: int,
	name: String,
	hidden_attrs: Object,
	user_attrs: Object
}
```
`lat` and `lon` are required. If multiple stops have the same `id` then only the first is used and the rest are ignored by BNOPI. If any `id` is `null` or `undefined` then BNOPI assigns a new id that is different to all others. `hidden_attrs` stores any data needed by the editing framework to reconstruct the primary instance after editing, but is not displayed to the user. `user_attrs` contains information that is displayed to the user and can be edited by the user.

`Route` is typed as
```
Route: {
	id: int,
	name: String,
	points: {lat: float, lon: float}[],
	hidden_attrs: Object
	user_attrs: Object,
}
```
where the `points` list is a list of geographical points that the route passes through. -->

This generates a list of `BNOPIStop`s and `BNOPIRoute`s from the input instances, which BNOPI then renders.

`BNOPIStop` is typed as

```typescript
type BNOPIStop = {
	lat: number;
	lon: number;
	id: number;
	name: string | undefined;
	hidden_attrs: any;
	user_attrs: any;
}
```

`lat` and `lon` are required. If multiple stops have the same `id` then only the first is used and the rest are ignored by BNOPI. If any `id` is `null` or `undefined` then BNOPI assigns a new id that is different to all others. `hidden_attrs` stores any data needed by the editing framework to reconstruct the primary instance after editing, but is not displayed to the user. `user_attrs` contains information that is displayed to the user and can be edited by the user.

`BNOPIRoute` is typed as

```typescript
type BNOPIRoute = {
    id: number;
    name: string | undefined;
    points: {
        lat: number;
        lon: number;
    }[];
    stops: number[];
    hidden_attrs: any;
    user_attrs: any;
}
```

where the `points` list is a list of geographical points that the route passes through, and `stops` is a list of stop ids, referencing `BNOPIStop`s.


## Procedure for editing a stage instance

Inside the interface stops/routes may be created/edited/deleted, and any attribute in `user_attrs` may be edited.

When the user saves changes to the stage instance, the **editing framework** for the stage is called. This is of the type:

```typescript
(method) editingFramework(primaryInstance: BNOPIInstance, requirementInstances: BNOPIInstance[], stops: BNOPIStop[], routes: BNOPIRoute[], stageFormatHandler: StageFormatHandler): {
	primaryData: (Buffer | null);
	requirementDatas: (Buffer | null)[] | null | undefined;
}
```

`primaryData` and `requirementDatas` are new versions of the files to reflect the changes the user has made to the `stops` and `routes`.

Any stop or route that was added by the user will be given an new unique stop id or route id *before* the editing framework is called.

BNOPI then writes the new stage instance to disk (at a location decided by BNOPI) and creates an accompanying *.stg.json* file.

## *.fmt.js* structure
A *.fmt.js* file is a module that exports a class that extends the `StageFormat` class, defined in [/main/js/stage_format_handler.js](/main/js/stage_format_handler.js). It has the following properties:

+ `name: String` - The name of the stage format
+ `id: String` - An id by which the stage is referred to. Usually an uppercase string separated by underscores, e.g. `"STOP_CONNECTION_GRAPH"`.
+ `requirements: String[]` - A list of stage format ids corresponding to the requirements of the display framework, as defined above.
+ `description: String` - A helpful description of the stage format
+ `fileExtension: String` - The preferred file extension for instances of this stage (without a dot before, i.e. just `"json"` for JSON files).
+ `displayFramework` - A function used to convert the instances something displayable by BNOPI (see above)
+ `editingFramework` - A function used to convert the BNOPI representation back to a stage instance.