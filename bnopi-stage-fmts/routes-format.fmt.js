const StopsFormat = require("./stops-format.fmt");



/**
 * Display a route network on the screen
 * 
 * @param {Buffer} data Route network buffer
 * @param {Buffer[2]} requirements 2 buffers, first contains the stop connection graph and the second contains the stops.
 */
function displayRoutes(data, requirements) {

	const routesData = data;
	const stopConnectionGraphData = requirements[0];
	const stopsData = requirements[1];

	// reuse the stops display framework to display the stops here
	const {stops} = StopsFormat.displayFramework(stopsData, []);

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
			hidden_attrs: {stops: route.stops, links:route.links}
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

	return {stops:stops, routes:routes}

}


/** Convert the on-screen stops to a format to be written as a stage instance
 * 
 * @param {Buffer} data Original version of the stops
 * @param {Buffer[]} requirements Original versions of the requirements of this stage format
 * @param {Array} stops All stops open in the map
 * @param {Array} routes All routes open in the map
 * @returns {Buffer} The new stage instance
 */
function exportRoutes(data, requirements, stops, routes) {

	// TODO
	// currently return original file unaltererd

	return data;
}

module.exports = {
	name: "Routes",
	id: "ROUTES",
	requirements:["STOP_CONNECTION_GRAPH", "STOPS"],
	description: "JSON file containing a route network, referencing the stop connection graph and stops.",
	fileExtension: "json",
	displayFramework: displayRoutes,
	editingFramework: exportRoutes
}

