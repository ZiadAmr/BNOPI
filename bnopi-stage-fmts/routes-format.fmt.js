const StopsFormat = require("./stops-format.fmt");
const { StageFormat } = require("../main/js/stage_format_handler");

/**
 * Format of data in stage instance JSON
 * @typedef {{id: number, name: string, length:number, speed:any: startid: number, endid: number, points: number[]}} SCGLink
 * @typedef {{id: number, lat: number, lon: number}} SCGPoint
 */

module.exports = class RoutesFormat extends StageFormat {
	static get name() {return "Routes"}
	static get id() {return "ROUTES"}
	static get requirements() { return ["STOP_CONNECTION_GRAPH", "STOPS"] }
	static get description() { return "JSON file containing a route network, referencing the stop connection graph and stops." }
	static get fileExtension() {return "json"}

	/**
	 * @type {StageFormat.displayFramework}
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
		/** @type {{links: SCGLink[], points: SCGPoint[]}} */
		const stopConnectionGraph = JSON.parse(decoder.decode(stopConnectionGraphData));


		// create map from the points and links
		/** @type {Map<number, SCGPoint>} */
		const points_map = new Map();
		/** @type {Map<number, SCGLink>} */
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
			var bnopiRoute = {
				id: route.id,
				name: route.name,
				links: [],
				stops: [],
				user_attrs: {},
				hidden_attrs: { stops: route.stops, links: route.links }
			};

			// convert each route to a sequence of links, themselves containing geographical points.
			for (const linkid of route.links) {
				const scgLink = links_map.get(linkid);
				bnopiRoute.stops.push(scgLink.startid);
				
				const bnopiLink = [];

				for (const pointid of scgLink.points) {
					const point = points_map.get(pointid);
					bnopiLink.push({
						lat: point.lat,
						lon: point.lon
					});
				}

				bnopiRoute.links.push(bnopiLink);
			}

			routes.push(bnopiRoute);
		}

		return { stops: stops, routes: routes }

	}

	/**
	 * @type {StageFormat.editingFramework}
	 */
	editingFramework(primaryInstance, requirementInstances, stops, routes, stageFormatHandler) {

		// TODO WIP!!

		const oldRoutesInstance = primaryInstance;
		const oldStopConnectionGraphInstance = requirementInstances[0];
		const oldStopsInstance = requirementInstances[1];

		// parse old requirement data
		const decoder = new TextDecoder('utf-8');
		const stopConnectionGraph = JSON.parse(decoder.decode(oldStopConnectionGraphInstance.data));

		// create map from the points and links
		const points_map = new Map();
		const links_map = new Map();
		for (let i = 0; i < stopConnectionGraph.points.length; i++) {
			points_map.set(stopConnectionGraph.points[i].id, stopConnectionGraph.points[i])
		}
		for (let i = 0; i < stopConnectionGraph.links.length; i++) {
			links_map.set(stopConnectionGraph.links[i].id, stopConnectionGraph.links[i])
		}

		// new stops file
		const newStopsInstance = StopsFormat.editingFramework(oldStopsInstance, [], stops, [], stageFormatHandler);


		for (const bnopiRoute of routes) {
			// search the dependency graph for links that go between these stops to make a continuous list of points
			// If there is a section that does not match then we add new links in the dependency graph for that section and use those instead.
			// ASSUMPTION: no new id was created that was the same as an old id that was deleted.


		}

		// for each link in the route check to see if it already exists

		return {primaryInstance: undefined};
	}
}
