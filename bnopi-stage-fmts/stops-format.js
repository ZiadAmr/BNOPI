
/**
 * Display stops on the screen
 * 
 * @param {string} data Contents of the stage instance file in string form
 */
function displayStops(data) {

	JSON.parse(data).stops.forEach(stop => {

		// create google maps marker.
		// keep the stop id for now in case it needs to be assigned a new id,
		// but note that the id will be reassigned when the stop stage instance is exported
		const position = { lat: stop.lat, lng: stop.lon };
		marker = new google.maps.Marker({
			position: position,
			map,
			title: "Bus stop",
			id: stop.id,
			name: stop.name,
			icon: {
				size: new google.maps.Size(50, 50),
				scaledSize: new google.maps.Size(50, 50),
				url: "icons/bus-station.png"
			}
		})

		// add the marker to the busStops hashmap
		busStops.set(marker.position, marker);
		google.maps.event.addListener(marker, 'click', function deleteMarker(event) {

			//The user has clicked the delete markers button 
			if (window.localStorage.getItem('mode') == 2) {
				busStops.get(event.latLng).setMap(null);
				busStops.delete(event.latLng);
			}
		});

	});
}

/**
 * Convert bus stops to JSON
 * 
 * @returns string containing the contents of the stage instance
 */
function exportStops() {

	var id_counter = 0;

	var stops = [];

	for (let stop of busStops.values()) {

		var lat = stop.position.lat();
		var lon = stop.position.lng();
		var name = "";
		if (stop.name != undefined) {
			name = stop.name;
		}
		var id = id_counter++;

		stops.push({
			"lat": lat,
			"lon": lon,
			"name": name,
			"id": id
		});

	}

	return JSON.stringify({ "stops": stops });

}


addStageFormat({
	"name": "Stops",
	"id": "STOPS",
	"description": "JSON file containing information about bus stops. See https://github.com/ZiadAmr/BNOPI/blob/main/stage-formats/2_generate_stops.json",
	"display-framework": displayStops,
	"editing-framework": exportStops
})