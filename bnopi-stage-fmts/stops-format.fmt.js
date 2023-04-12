

const {StageFormat} = require("../main/js/stage_format_handler");


module.exports = class StageFormatImpl extends StageFormat {

	static get name() {return "Stops"}
	static get id() {return "STOPS"}
	static get requirements() {return []}
	static get description() { return "JSON file containing information about bus stops. See https://github.com/ZiadAmr/BNOPI/blob/main/stage-formats/2_generate_stops.json" }
	static get fileExtension() {return "json"}

	/** 
	 * @inheritdoc
	 */
	static displayFramework(primaryInstance) {

		const decoder = new TextDecoder('utf-8')

		// convert buffer to string
		const stopsString = decoder.decode(primaryInstance.data);

		// what we want to display
		var stops = [];

		// add each stop from the file
		JSON.parse(stopsString).stops.forEach(stop => {
			stops.push({
				lat: stop.lat,
				lon: stop.lon,
				id: stop.id,
				name: stop.name,
				user_attrs: {},
				hidden_attrs: {}
			});
		});

		return { stops: stops, routes: [] }
	}

	/**
	 * @inheritdoc
	 */
	static editingFramework(primaryInstance, requirementInstances, stops) {

		// BNOPI will assign new ids to each stop we add so we don't need to worry about that.

		var exportStops = [];
		stops.array.forEach(stop => {
			exportStops.push({
				name: stop.name,
				id: stop.id,
				lat: stop.lat,
				lon: stop.lon
			});
		});

		return {primaryInstance: Buffer.from(JSON.stringify(exportStops))};
	}
} 

