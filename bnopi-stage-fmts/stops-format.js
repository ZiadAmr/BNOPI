
/**
 * Display stops on the screen
 * 
 * @param {Buffer} data Contents of the stage instance file in string form
 */
function displayStops(data) {

	// convert buffer to string
	const stopsString = decoder.decode(data.data);

	// what we want to display
	var stops = [];

	// add each stop from the file
	JSON.parse(stopsString).stops.forEach(stop => {
		stops.push({
			lat: stop.lat,
			lon: stop.lon,
			id: stop.id,
			user_attrs: {
				name: stop.name
			},
			hidden_attrs: {}
		});
	});

	return { stops: stops, routes: {} }
}

/**
 * 
 * @param {Buffer} data Original version of the file
 * @param {*} stops All stops open in the map
 * @param {*} routes All routes open in the map
 * @returns {Buffer} The new stage instance
 */
function exportStops(data, stops, routes) {

	// BNOPI will assign new ids to each stop we add so we don't need to worry about that.

	var exportStops = [];
	stops.array.forEach(stop => {
		exportStops.push({
			name: stop.hidden_attrs.name,
			id: stop.id,
			lat: stop.lat,
			lon: stop.lon
		});
	});

	return Buffer.from(JSON.stringify(exportStops));

}


addStageFormat({
	"name": "Stops",
	"id": "STOPS",
	"description": "JSON file containing information about bus stops. See https://github.com/ZiadAmr/BNOPI/blob/main/stage-formats/2_generate_stops.json",
	"display-framework": displayStops,
	"editing-framework": exportStops
})