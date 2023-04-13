const StopsFormat = require("./stops-format.fmt");
const { StageFormat } = require("../main/js/stage_format_handler");
const { GeoCoordinate } = require('geocoordinate');

/**
 * Format of data in stage instance JSON
 * @typedef {{id: number, name: string, length:number, speed:any: startid: number, endid: number, points: number[]}} SCGLink
 * @typedef {{id: number, lat: number, lon: number}} SCGPoint
 * @typedef {{links: SCGLink[], points: SCGPoint[]}} SCG
 * @typedef {{id: number, name: string, stops: number[], links: number[]}} RNRoute Route network route (how they are stored in the stage instance)
 * @typedef {{routes: RNRoute[]}} RN Route network stage instance contents
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
		/** @type {SCG} */
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
		/** @type {SCG} */
		const stopConnectionGraph = JSON.parse(decoder.decode(oldStopConnectionGraphInstance.data));

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

		// create map from stops
		/** @type {Map<number, BNOPIStop>} */
		const stops_map = new Map();
		for (const stop of stops) {
			stops_map.set(stop.id, stop);
		}

		/**
		 * Map of fromStops to list of links in stop connection graph
		 * @type {Map<number, SCGLink[]>}
		 */
		const outgoingLinksMap = new Map();
		for (const link of stopConnectionGraph.links) {
			if (outgoingLinksMap.has(link.startid)) {
				outgoingLinksMap.get(link.startid).push(link);
			} else {
				outgoingLinksMap.set(link.startid, [link]);
			}
		}

		// new stops file
		const newStopsData = StopsFormat.editingFramework(oldStopsInstance, [], stops, [], stageFormatHandler).primaryData;




		/** create new routes stage instance
		 * @type {RN} 
		 */
		const newRoutesInstance = {routes: []};

		// id numbers in case we need to add new links or points
		var newLinkId = Math.max(links_map.keys()) + 1;
		var newPointId = Math.max(points_map.keys()) + 1;

		var scgModified = false;


		for (const bnopiRoute of routes) {

			/**
			 * Route to add to new routes stage instance
			 * @type {RNRoute}
			 */
			const newRoute = {
				id: bnopiRoute.id,
				name: bnopiRoute.name,
				stops: bnopiRoute.stops,  
				links: [] // add these next
			};


			// search the dependency graph for links that go between these stops to make a continuous list of points
			// If there is a section that does not match then we add a new link in the dependency graph for that section and use those instead.
			// ASSUMPTION: no new id was created that was the same as an old id that was deleted.

			for (let i = 0; i < bnopiRoute.links.length; i++) {
				const fromStop = bnopiRoute.stops[i];
				const toStop = bnopiRoute.stops[i+1];
				const link = bnopiRoute.links[i];

				// look for this edge in the old stop connection graph
				/** @type {SCGLink | undefined} */
				let matchingLink;
				if (outgoingLinksMap.has(fromStop)) {
					matchingLink = outgoingLinksMap.get(fromStop).find(scgLink => {
						// link must have the same end id
						if (scgLink.endid != toStop) return false;

						// the points in the link must match closely (accounting for floating point errors)
						if (scgLink.points.length != link.length) return false;
						for (let j = 0; j < link.length; j++) {
							const scgPoint = points_map.get(scgLink.points[i]);
							const point = link[i];

							if (Math.abs(scgPoint.lat - point.lat) > 0.00001) return false;
							if (Math.abs(scgPoint.lon - point.lon) > 0.00001) return false;
							
						}
						
						// passed test - this SCG link must match the poly line drawn.
						return true;


					});
				}

				var scgLink = matchingLink;

				// if there was no matching link then create one.
				if (typeof matchingLink === "undefined") {
					// add new link to the SCG
					
					// give points new ids
					/** @type {SCGPoint[]} */
					const newPoints = link.map(pt => ({
						id: newPointId++,
						lat: pt.lat,
						lon: pt.lon
					}));

					// work out length of link in km.
					var linkLength = 0;
					for (let j = 0; j < link.length-1; j++) {
						linkLength += (new GeoCoordinate(link[i].lat, link[i].lon)).distanceTo(new GeoCoordinate(link[i+1].lat, link[i+1].lon)) / 1000;
					}
					
					/** @type {SCGLink} */
					const newLink = {
						id: newLinkId++,
						name: stops_map.get(fromStop).name + " => " + stops_map.get(toStop).name,
						length: linkLength,
						speed: { "0:00": 30 }, // not implemented, assume 30mph everywhere
						startid: fromStop,
						endid: toStop,
						points: newPoints.map(pt => pt.id)
					}

					// add the new link and points to the hashmaps.
					newPoints.forEach(pt => {
						points_map.set(pt.id, pt)
					});
					links_map.set(newLink.id, newLink);
					scgModified = true;

					scgLink = newLink;
				}


				// now scgLink refers to the right link. Add this to the newRoute in the stage instance.
				newRoute.links.push(scgLink.id);
				
			}

			newRoutesInstance.routes.push(newRoute);
		}

		// we already have the new points instance. Now create new SCG and routes instances.
		// new stop connection graph
		var newSCGData = null;
		if (scgModified) {
			const newSCGInstance = {
				// sort in order of ascending id
				links: Array.from(links_map.values()).sort((l0, l1) => l0.id - l1.id),
				points: Array.from(points_map.values()).sort((p0, p1) => p0.id - p1.id)
			};
			newSCGData = Buffer.from(JSON.stringify(newSCGInstance));
		}

		// new routes
		const newRoutesData = Buffer.from(JSON.stringify(newRoutesInstance));

		return { primaryData: newRoutesData, requirementDatas: [newSCGData, newStopsData]};
	}
}
