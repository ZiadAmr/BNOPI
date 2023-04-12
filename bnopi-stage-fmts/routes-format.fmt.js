const StopsFormat = require("./stops-format.fmt");
const { StageFormat } = require("../main/js/stage_format_handler");

module.exports = class StageFormatImpl extends StageFormat {
	static get name() {return "Routes"}
	static get id() {return "ROUTES"}
	static get requirements() { return ["STOP_CONNECTION_GRAPH", "STOPS"] }
	static get description() { return "JSON file containing a route network, referencing the stop connection graph and stops." }
	static get fileExtension() {return "json"}

	/**
	 * @inheritdoc
	 */
	static displayFramework(primaryInstance, requirementInstances) {

		const routesData = primaryInstance.data;
		const stopConnectionGraphData = requirementInstances[0].data;
		const stopsData = requirementInstances[1].data;

		// reuse the stops display framework to display the stops here
		const { stops } = StopsFormat.displayFramework(requirementInstances[1], []);

		// parse the JSON files
		const decoder = new TextDecoder('utf-8');
		const routenet = JSON.parse(decoder.decode(routesData));
		const stopConnectionGraph = JSON.parse(decoder.decode(stopConnectionGraphData));


		// create map from the points and links
		const points_map = new Map();
		const links_map = new Map();
		for (let i = 0; i < stopConnectionGraph.points.length; i++) {
			points_map.set(stopConnectionGraph.points[i].id, stopConnectionGraph.points[i])
		}
		for (let i = 0; i < stopConnectionGraph.links.length; i++) {
			links_map.set(stopConnectionGraph.links[i].id, stopConnectionGraph.links[i])
		}

		var routes = [];

		for (const route of routenet.routes) {
			// setup BNOPI route
			var BNOPIRoute = {
				id: route.id,
				name: route.name,
				points: [],
				user_attrs: {},
				hidden_attrs: { stops: route.stops, links: route.links }
			};

			// convert each route to a sequence of geographical points
			for (const linkid of route.links) {
				for (const pointid of links_map.get(linkid).points) {
					const point = points_map.get(pointid);
					BNOPIRoute.points.push({
						lat: point.lat,
						lon: point.lon
					});
				}
			}

			routes.push(BNOPIRoute);
		}

		return { stops: stops, routes: routes }

	}

	/**
	 * @inheritdoc
	 */
	editingFramework() {
		return {primaryInstance: undefined};
	}
}
