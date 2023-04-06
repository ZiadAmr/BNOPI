# Stage Formats

The user selects to open a stage instance, or something else opens a stage instance. At this point the stage tracker is displaying a list of .stg.json files which contains some metadata and point to the actual stage instance.

BNOPI reads the .stg.json file to get 2 important bits of information, the stage format and the location of the stage instance.

BNOPI then checks if there exists a stage format that matches. Stage formats are stored in a single js file and are added to the main program via api call, which also passes the functions that handler display and editing frameworks.

If the stage format exists, then BNOPI reads the stage instance into a buffer and calls the display framework function. This will be of the type

	displayX(data: buf) -> {stops:[...], routes:[...]}

where each stop is of the form:
```
{
	lat:
	lon:
	id:
	hidden_attrs: {...},
	user_attrs: {...}
}
```
`lat` and `lon` are required. If multiple stops have the same `id` then only the first is used and the rest are ignored by BNOPI. If any `id` is null then BNOPI assigns a new id that is different to all others. `hidden_attrs` stores any data needed by the editing framework to reconstruct the file, but is not displayed to the user. `user_attrs` contains information that is displayed to the user inside the interface when the stop is selected.

.. and where each route is of the form:
```
{
	id:
	points:[...],
	hidden_attrs:
	user_attrs,
}
```
each point in `points` is of the form `{lat:, lon:}`.


BNOPI then renders these appropriately. Inside the interface stops/routes may be created/deleted, and any attribute in `user_attrs` may be edited.

When the user saves changes to the stage instance, the editing framework for the stage is called. This is of the form:

	editX(data:buf, stops, routes) -> buf

where `data` is the original unedited version of the file, and the function output is the new version of the data.

BNOPI then writes the new stage instance to disk and creates an accompanying .stg.json file.