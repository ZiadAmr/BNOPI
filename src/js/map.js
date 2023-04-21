/**
 * Instance type passed to display and editing frameworks
 * @typedef {{data: Buffer, metadata: InstanceMetadata, metadataFilePath: String}} BNOPIInstance
 */

/**
 * Contents of a stage instance metadata file
 * @typedef {{timeCreated: string, dependencyGraph: string, format: string, generatedBy: string, nodeInGraph:(number|null), parentStageInstances:string[], siblingStageInstances:string[], datafile:string}} InstanceMetadata
 */

/**
 * A bus stop in the format used to communicate with the render
 * @typedef {{lat: number; lon: number; id: number; name: string | undefined; hidden_attrs: any; user_attrs: any;}} BNOPIStop
 */


/**
 * A bus route in the format used to communicate with the renderer
 * @typedef {{id: number; name: string | undefined; links: {lat: number; lon: number;}[][], stops:number[], hidden_attrs: any, user_attrs: any}} BNOPIRoute
 */

/**
 * A bus route in the format used to display on the screen
 * @typedef {{id: number; name: string | undefined; links: google.maps.Polyline[], continuityLinks: google.maps.Polyline[], stops:number[], hidden_attrs: any, user_attrs: any}} DisplayRoute
 */






//Variable storing the google maps embedding
var map;

//Code used for polylines (drawing a route on the map was directly referenced from google maps documentation)
//https://developers.google.com/maps/documentation/roads/snap
var apiKey = 'AIzaSyAWmWHoyHgni9A2p4kYBloFIuTeE4linzo';
var drawingManager;
var snappedCoordinates = [];

// Variables used in the draw route tool
var current_route_draw = [];    // Information about the current route that is being drawn
var display_polyline = null;  // Information on the current polyline that is being rendered whilst a route is being drawn
var current_link = [];  // Information on the latlng points of the current pair of bus stops  
var stops_track = [];   // Information on the stops that have been placed during route draw
var links_track = [];   //Information on the links that have been generated during the route draw




//Elements relating to editing a polyline
var selectedPolyline = null;    //When a user clicks on another polyline after editing one (instead of clicking save), this variable will be used to change the setting to editable = false

//Code for styling the map
var styleArray = [
    { featureType: "poi", stylers: [{ visibility: "off" }] },
    { featureType: "transit", stylers: [{ visibility: "on" }] }
];

function initMap() {
    var optionParams = {
        zoom: 14,
        center: { lat: 52.52955, lng: -1.22395 },
        mapTypeId: "terrain"
    };

    map = new google.maps.Map(document.getElementById('map'), optionParams);
    //Ensures the map only displays roads
    map.setOptions({ styles: styleArray });

    // Create a bus stop when the bus stop tool is selected
    google.maps.event.addListener(map, 'click',
        function (event) {
            if (window.localStorage.getItem('mode') == 1) {
                displayBNOPIStop({
                    lat: event.latLng.lat(),
                    lon: event.latLng.lng(),
                    id: newUniqueStopID(),
                    name: "Custom stop",
                    hidden_attrs: {},
                    user_attrs: {}
                })
            }else if(window.localStorage.getItem('mode') == 3){
                var new_click = new CustomEvent('mapClick', {detail: {type:'path_point', values:event}});
                window.dispatchEvent(new_click)
            }
        });

    // Adds a bus stop when right clicked on the map whilst the route draw tool is selected
    google.maps.event.addListener(map, 'rightclick',
        function (event) {
            if (window.localStorage.getItem('mode') == 3) {
                const stop = displayBNOPIStop({
                    lat: event.latLng.lat(),
                    lon: event.latLng.lng(),
                    id: newUniqueStopID(),
                    name: "Custom stop",
                    hidden_attrs: {},
                    user_attrs: {}
                });

                var new_click = new CustomEvent('mapClick', {detail: {type:'bus_stop', values:event, ID:stop.id}});
                window.dispatchEvent(new_click)
            }
        });


    // add open project event listener
    window.electron.onOpenProject((_event, projPath) => openProject(projPath));
    window.electron.onSave(() => {
        if (modifiedStageInstance) {
            saveStageInstanceAs(currentStageInstance.instanceMetdataPath, currentStageInstance.requirementMetadataPaths);
        }
    })
    window.addEventListener("displayStageInstance", (event) => displayStageInstance(event.detail.instanceMetdataPath, event.detail.requirementMetadataPaths));

    window.addEventListener("bus_stops_change", event => { setModified() });
    window.addEventListener("routes_change", event => { setModified() });

}

function newUniqueStopID() {
    var newID = 1;
    if (busStops.size > 0) {
        // one higher than highest existing id
        newID = Math.max(...Array.from(busStops.values()).map(b => b.id)) + 1;
    }
    return newID;
}

/** Update the global variable stageInstances, and update stage tracker
 * 
 * @param {string} projPath 
 */
async function reloadStageTracker(projPath) {
    // get list of stage instances
    /**
    * @typedef {{name: string;id: string; requirements: string[]; description: string; fileExtension: string;}} StageFormatInfo
    * @type {{path: string, metadata: InstanceMetadata, stageFormatInfo: StageFormatInfo|undefined}[]} 
    * */
    const newStageInstances = await window.electron.getListOfStageFormat(projPath);

    // load any additional algorithms and formats specified in the info folder TODO

    // get dependency graph (not implemented)
    // TODO

    // add info about the stage formats to each instance
    for (const inst of newStageInstances) {
        inst.stageFormatInfo = await window.electron.getStageFormatInfo(inst.metadata.format);
    }


    // clear the stage tracker and add the list of stages to it
    stageInstances = newStageInstances;
    // call something to update the react code
    window.dispatchEvent(new Event('stage_instances_change'));
}

async function openProject(projPath) {
    // save and close any prject that might already be open TODO.

    // add this project to the recents
    await window.electron.addToRecents(projPath);

    // get the project metadata
    const projMetadata = await window.electron.getProjectMetadata(projPath);
    

    await reloadStageTracker(projPath);
    

    console.log(stageInstances)
    console.log(projMetadata);

    // set global variable
    projectPath = projPath;

    // TODO hard code it to open the route network
    const routesInstancePath = stageInstances.find((ins) => ins.path.split('\\').pop().split('/').pop() == "routes.stg.json").path;
    const requirementMetadataPaths = [
        stageInstances.find((ins) => ins.path.split('\\').pop().split('/').pop() == "stop-connection-graph.stg.json").path,
        stageInstances.find((ins) => ins.path.split('\\').pop().split('/').pop() == "stops.stg.json").path, 
    ];
    displayStageInstance(routesInstancePath, requirementMetadataPaths);



    // const re = /STOPS_1/;
    // const stopsInstance = stageInstances.find((ins) => ins.path.match(re) != null);
    // displayStageInstance(stopsInstance.path);
    // console.log(polyMap);
    return null;


}

async function displayStageInstance(instanceMetdataPath, requirementMetadataPaths) {

    // save the currently open stage instance
    if (autoSave && isDisplayingStageInstance && modifiedStageInstance) {
        // display confirmation dialog
        const choice = await window.electron.showMessageBox({
            type: "question",
            buttons: ["Save", "Don't save", 'Cancel'],
            message: 'The stage instance has been edited. Save changes?',
            // detail: "",
            defaultId: 0,
            cancelId: 2,
        });

        switch (choice.response) {
            case 0 /*save*/:
                await saveStageInstanceAs(currentStageInstance.instanceMetdataPath, currentStageInstance.requirementMetadataPaths);
                break;
            
            case 1 /*don't save*/:
                break;
        
            default:
                return; // don't display the new stage instance.
        }



    }

    // clear any stage instance already diplaying
    busStops.forEach(stop => {
        stop.setMap(null);
    });
    Array.from(routeMap.keys()).forEach(displayRoute => {
        deleteDisplayRoute(displayRoute);
    })
    busStops.clear();
    routeMap.clear();

    // call display framework
    const {stops, routes} = await window.electron.loadStageInstance(instanceMetdataPath, requirementMetadataPaths);

    // render
    for (const stop of stops) {
        displayBNOPIStop(stop);
    }
    for (const route of routes) {
        displayBNOPIRoute(route);
    }
    
    // store the metadata file paths
    isDisplayingStageInstance = true;
    currentStageInstance = {
        instanceMetdataPath: instanceMetdataPath,
        requirementMetadataPaths: requirementMetadataPaths
    };

    window.dispatchEvent(new Event("bus_stops_change"));
    window.dispatchEvent(new Event('routes_change'));
    setUnmodified();
}

/**
 * Save the currently displaying stage instance
 * @param {string} oldPrimPath The path to the former primary instance (before the user made any edits) in the stage format that is currently display
 * @param {string[]} oldReqPaths Paths to former requirement instances for the stage formats
 */
async function saveStageInstanceAs(oldPrimPath, oldReqPaths) {

    // convert to bnopi stops and routes
    let {BNOPIStops, BNOPIRoutes} = getCurrentlyDisplaying();

    // remove routes that contain null stops
    BNOPIRoutes = BNOPIRoutes.filter(bnopiRoute => {
        if (bnopiRoute.stops.some(stop => stop === null)) {
            console.warn(`Route with id ${bnopiRoute.id} and name \"${bnopiRoute.name}\" contained a null stop and was deleted.`);
            return false;
        }
        return true;
    });


    const { newestPrimaryMetadataPath, newestRequirementsMetadataPaths } = await window.electron.saveStageInstanceAs(oldPrimPath, oldReqPaths, BNOPIStops, BNOPIRoutes);

    console.log("The newest versions of the stage instances are now ", newestPrimaryMetadataPath, newestRequirementsMetadataPaths);

    // reopen new version of instance
    setUnmodified(); // prevent auto save
    displayStageInstance(newestPrimaryMetadataPath, newestRequirementsMetadataPaths);

    // update stageInstances variable and stage tracker
    await reloadStageTracker(projectPath);

}


/** Display a bus stop from the BNOPI format (that which is received from the stage format handler).
 * Converts the stop into a google maps marker and adds to hashmap / screen
 * 
 * @param {{lat: number; lon: number; id: number; name: string | undefined; hidden_attrs: any; user_attrs: any;}} stop Stop in BNOPI format
 * @returns {google.maps.Marker}
 */
function displayBNOPIStop(stop) {
    // if the bus stop doesn't have a name just use the id
    var name = stop.name;
    if (typeof name === "undefined") {
        name = stop.id;
    }

    marker = new google.maps.Marker({
        position: {
            lat: stop.lat,
            lng: stop.lon
        },
        map,
        title: "Bus stop",
        id: stop.id,
        name: name,
        icon: {
            size: new google.maps.Size(30, 30),
            scaledSize: new google.maps.Size(30, 30),
            url: "icons/bus-station.png"
        }
    });
    marker.bnopiUserAttrs = stop.user_attrs;
    marker.bnopiHiddenAttrs = stop.hidden_attrs;

    // add the marker to the busStops hashmap
    busStops.set(marker.position, marker);
    window.dispatchEvent(new Event('bus_stops_change'));
    google.maps.event.addListener(marker, 'click', function deleteMarker(event) {

        //The user has clicked the delete markers button 
        if (window.localStorage.getItem('mode') == 2) {

            // if this stop is part of a route then merge the links on either side of it.

            for (const route of Array.from(routeMap.values())) {
                var i = 0;
                while (i < route.stops.length) {
                    if (route.stops[i] == stop.id) {
                        // prevent route from becoming singleton.
                        if (route.stops.length <= 2) {
                            deleteDisplayRoute(route.id);
                            break;
                        }
                        // if this is at the start or end of the array delete the link.
                        else if (i == 0) {
                            route.stops.splice(i, 1);
                            route.links[i].setMap(null);
                            route.links.splice(i, 1);
                            route.continuityLinks[i].setMap(null);
                            route.continuityLinks.splice(i,1);
                        } else if (i == route.stops.length-1) {
                            route.stops.splice(i, 1);
                            route.links[i-1].setMap(null);
                            route.links.splice(i-1, 1);
                            route.continuityLinks[i - 2].setMap(null);
                            route.continuityLinks.splice(i-2, 1);
                        } else {
                            // otherwise merge two links on either side of the stop
                            route.stops.splice(i,1);
                            route.continuityLinks[i - 1].setMap(null);
                            route.continuityLinks.splice(i - 1, 1);
                            
                            // extend the first link with the second
                            const path = route.links[i - 1].getPath();
                            route.links[i].getPath().forEach(pt => {
                                path.push(new google.maps.LatLng(pt.lat(), pt.lng()))
                            })

                            route.links[i].setMap(null);
                            route.links.splice(i, 1);


                        }
                        updateContinuityLinks(route);
                    } else {
                        i++;
                    }
                }
            }


            busStops.get(event.latLng).setMap(null);
            busStops.delete(event.latLng);

            window.dispatchEvent(new Event('bus_stops_change'));
        }
    });

    window.dispatchEvent(new Event('bus_stops_change'));

    return marker;

}

/**
 * Display a route from the BNOPI format (that which is received from the stage format handler).
 * 
 * @param {BNOPIRoute} route Route in BNOPI format
 */
function displayBNOPIRoute(route) {

    var name = route.name;
    if (typeof name === "undefined") {
        name = route.id;
    }

    const color = "#" + Math.floor(Math.random() * 16777215).toString(16);

    /** @type {google.maps.Polyline[]} */
    const links = route.links.map(link => {

        // create poly line
        polyLine = new google.maps.Polyline({
            path: link.map(pt => new google.maps.LatLng(pt.lat,pt.lon)),
            strokeColor: color,
            strokeWeight: 8,
            strokeOpacity: 1,
        });
        polyLine.setMap(map);

        // add event listeners
        polyLine.addListener("click", function() {

            if (window.localStorage.getItem('mode') == 4 /*delete route*/) {
                // delete entire route
                deleteDisplayRoute(route.id);

            } else if (window.localStorage.getItem('mode') == 5 /*edit route*/) {
                this.setOptions({ editable: true });
                //If the user had clicked on another polyline before (make that previous polyline uneditable)
                if (selectedPolyline != null) {
                    selectedPolyline.setOptions({ editable: false });
                }
                selectedPolyline = this;
            }
        });

        // listeners for edits.
        polyLine.getPath().addListener('insert_at', function () {
            setModified();
        });
        polyLine.getPath().addListener('set_at', function () {
            setModified();
        });
        polyLine.getPath().addListener('remove_at', function () {
            setModified();
        });
        polyLine.getPath().addListener('dragend', function () {
            setModified();
        });

        return polyLine;

    });

    // dashed line to use for continuity lines
    const lineSymbol = {
        path: "M 0,-1 0,1",
        strokeOpacity: 1,
        strokeColor: color,
        strokeWeight: 8,
        scale: 4,
    };


    /** @type {google.maps.Polyline[]} */
    const continuityLinks = [];
    for (let i = 0; i < links.length-1; i++) {
        const thisLink = links[i];
        const nextLink = links[i+1];

        // create continuity poly line between each link of the route
        const polyLine = new google.maps.Polyline({
            path: [
                thisLink.getPath().getAt(thisLink.getPath().getLength()-1),
                nextLink.getPath().getAt(0)
            ],
            strokeColor: color,
            strokeWeight: 8,
            strokeOpacity: 0,
            icons: [
                {
                    icon: lineSymbol,
                    offset: "10px",
                    repeat: "20px",
                },
            ],

        });

        polyLine.setMap(map);

        // listener to delete route
        polyLine.addListener("click", function () {
            if (window.localStorage.getItem('mode') == 4 /*delete route*/) {
                // delete entire route
                deleteDisplayRoute(route.id);
            } 
        });

        continuityLinks.push(polyLine);
        
    }


    // convert to DisplayRoute - this is how it is stored
    /** @type {DisplayRoute} */
    const newRoute = {
        id:route.id,
        name:route.name,
        stops:route.stops,
        links: links,
        continuityLinks: continuityLinks,
        hidden_attrs: route.hidden_attrs,
        user_attrs: route.user_attrs
    }

    // listeners to update continuity links
    newRoute.links.forEach(link =>
        link.getPath().addListener('set_at', () =>
            updateContinuityLinks(newRoute)
        )
    )

    routeMap.set(route.id, newRoute);
    window.dispatchEvent(new Event('routes_change'));


}

/** Update endpoints of continuity links in a route.
 * 
 * @param {DisplayRoute} route 
 */
function updateContinuityLinks(route) {
    for (let j = 0; j < route.links.length - 1; j++) {
        const pt = route.links[j].getPath().getAt(route.links[j].getPath().getLength() - 1);
        route.continuityLinks[j].getPath().setAt(0, pt);
    }
    for (let j = 1; j < route.links.length; j++) {
        const pt = route.links[j].getPath().getAt(0);
        route.continuityLinks[j - 1].getPath().setAt(1, pt);
    }
}

/**
 * Deletes a route from the map
 * @param {number} id 
 */
function deleteDisplayRoute(id) {
    /** @type {DisplayRoute} */
    const thisDisplayRoute = routeMap.get(id);
    thisDisplayRoute.links.forEach(pL => {
        pL.setMap(null);
    });
    thisDisplayRoute.continuityLinks.forEach(pL => {
        pL.setMap(null);
    });
    routeMap.delete(id);
    setModified();
    window.dispatchEvent(new Event('routes_change'));
}


/** Collects the stops and routes currently displaying on the screen
 * 
 * @returns {{BNOPIStops: BNOPIStop[], BNOPIRoutes: BNOPIRoute[]}}
 */
function getCurrentlyDisplaying() {

    // convert to bnopi stops and routes
    const BNOPIStops = Array.from(busStops.values()).map(marker => ({
        lat: marker.getPosition().lat(),
        lon: marker.getPosition().lng(),
        id: marker.id,
        name: marker.name,
        hidden_attrs: marker.bnopiHiddenAttrs,
        user_attrs: marker.bnopiUserAttrs
    }));

    // const BNOPIRoutes = Array.from(polyMap.values()).map(polyLine => {
    //     const points = [];
    //     polyLine.getPath().forEach(googlePoint => {
    //         points.push({
    //             lat: googlePoint.lat(),
    //             lon: googlePoint.lng()
    //         });
    //     });
    //     return {
    //         id: polyLine.id,
    //         name: polyLine.name,
    //         // points: points,
    //         stops: polyLine.stops,
    //         links: polyLine.links, // this needs to be updated by the front end. It needs to know which section of the polyline has been changed, and then make the changes within the polyLine.links property.
    //         hidden_attrs: polyLine.bnopiHiddenAttrs,
    //         user_attrs: polyLine.bnopiUserAttrs
    //     }
    // });

    /** @type {BNOPIRoute[]}*/
    const BNOPIRoutes = Array.from(routeMap.values()).map(displayRoute => ({
        hidden_attrs: displayRoute.hidden_attrs,
        id: displayRoute.id,
        links: displayRoute.links.map(polyLine => {
            // convert PolyLine to list of {lat, lon}
            const bnopiLink = [];
            polyLine.getPath().forEach(googlePoint => {
                bnopiLink.push({
                    lat: googlePoint.lat(),
                    lon: googlePoint.lng()
                });
            });
            return bnopiLink;
        }),
        name: displayRoute.name,
        stops: displayRoute.stops,
        user_attrs: displayRoute.user_attrs
    }));

    return {BNOPIStops, BNOPIRoutes}

}

function stopsToJson() {

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

    return { "stops": stops };
}


//Called when a button from the network toolkit is clicked
function changeMode(newMode) {
    //If the last mode the program was in was add route mode, we need to disable the drawing manager
    if (window.localStorage.getItem('mode') == 3) {
        disableRouteDraw();
    } else if (window.localStorage.getItem('mode') == 5) {

        if (selectedPolyline != null) {
            selectedPolyline.setOptions({ editable: false });
            selectedPolyline = null;
        }
    }

    //Double clicking on the same button means the user has deactivated the tool
    if (window.localStorage.getItem('mode') == newMode) {
        window.localStorage.setItem('mode', 0);
        //If clicking from a different tool active or no tool active must set the tool related to the clicked button active 
    } else {
        window.localStorage.setItem('mode', newMode);
    }

    //If the new mode is 3 we need to start the drawing manager
    if (window.localStorage.getItem('mode') == 3) {
        enableRouteDraw();
    }
}

// Function used for drawing bus stops and routes on the map
function draw_tool(event){
    const lat = event.detail.values.latLng.lat()
    const lon = event.detail.values.latLng.lng()

    // Initial click should always be a stop
    if(current_route_draw.length === 0){
        if(event.detail.type === "bus_stop"){
            stops_track.push(event.detail.ID)
        }else{
            const stop = displayBNOPIStop({
                lat: event.detail.values.latLng.lat(),
                lon: event.detail.values.latLng.lng(),
                id: newUniqueStopID(),
                name: "Custom stop",
                hidden_attrs: {},
                user_attrs: {}
            });
            stops_track.push(stop.id)
        }
        current_link.push({lat, lon})
    }else{
        if(event.detail.type === "bus_stop"){
            stops_track.push(event.detail.ID);
            current_link.push({lat, lon});
            links_track.push(current_link);
            current_link = []
            current_link.push({lat, lon})
        }else{
            current_link.push({lat,lon});
        }
    }

    current_route_draw.push(event.detail.values.latLng);

    // Dynamically draw the polyline whilst in the draw tool
    if(current_route_draw.length > 1){
        if(display_polyline != null){
            display_polyline.setMap(null)
        }
        
        display_polyline = new google.maps.Polyline({
            path: current_route_draw,
            geodesic: true,
            strokeColor: '#FF0000',
            strokeOpacity: 1.0,
            strokeWeight: 4
        });

        display_polyline.setMap(map);
    }
}

//This code is part of google maps stick to road documentation (include that in the report references)
//Once the draw a route button is clicked, this function will be called
function enableRouteDraw() {
    window.addEventListener('mapClick', draw_tool);

    // Make the done button appear
    var done_button = new CustomEvent('done_button', {detail: {status:true}});
    window.dispatchEvent(done_button)
}

function disableRouteDraw() {
    // Make the done button disappear
    var done_button = new CustomEvent('done_button', {detail: {status:false}});
    window.dispatchEvent(done_button)

    if(current_route_draw.length > 1){
        // If the last point is not a stop, manually add a stop at the last point
        if(current_link.length > 1){
            const stop = displayBNOPIStop({
                lat: current_link[current_link.length - 1].lat,
                lon: current_link[current_link.length - 1].lon,
                id: newUniqueStopID(),
                name: "Custom stop",
                hidden_attrs: {},
                user_attrs: {}
            });
            // Add the new stop to the list of stops in the route
            stops_track.push(stop.id)
            // Add the link to the list of links
            links_track.push(current_link)
        }

        // Remove the event listener
        window.removeEventListener('mapClick', draw_tool);

        // Remove the temporary polyline which was drawn to give the user a reference
        if(display_polyline != null){
            display_polyline.setMap(null);
        }

        // Construct an actual route from the data gathered from the drawing tool
        // Generate a unique ID by adding 1 to the route with highest route ID
        var newID = 1;
        if(routeMap.size > 0){
            newID = Math.max(...Array.from(routeMap.values()).map(b => b.id)) + 1;
        }

        const new_route = {id:newID, name:"custom_route-" + newID.toString(), links:links_track, stops:stops_track, hidden_attrs:[], user_attrs: []}
        displayBNOPIRoute(new_route)

    }else if(current_route_draw.length === 1){
        // If the user has clicked once on the map in the draw tool and then finishes we have to delete the bus stop created
        busStops.get(current_route_draw[current_route_draw.length - 1]).setMap(null);
        busStops.delete(current_route_draw[current_route_draw.length - 1]);
        window.dispatchEvent(new Event('bus_stops_change'));
    }

    // Reset the variables used so the next time tool is selected it work correctly
    current_route_draw = [];
    display_polyline = null;
    current_link = []
    stops_track = [];
    links_track = [];
}

// Snap a user-created polyline to roads and draw the snapped path
function runSnapToRoad(path) {
    var pathValues = [];
    for (var i = 0; i < path.getLength(); i++) {
        pathValues.push(path.getAt(i).toUrlValue());
    }

    $.get('https://roads.googleapis.com/v1/snapToRoads', {
        interpolate: true,
        key: apiKey,
        path: pathValues.join('|')
    }, function (data) {
        processSnapToRoadResponse(data);
        drawSnappedPolyline();
    });
}

// Store snapped polyline returned by the snap-to-road service.
function processSnapToRoadResponse(data) {
    snappedCoordinates = [];
    for (var i = 0; i < data.snappedPoints.length; i++) {
        var latlng = new google.maps.LatLng(
            data.snappedPoints[i].location.latitude,
            data.snappedPoints[i].location.longitude);
        snappedCoordinates.push(latlng);
    }
}

// Draws the snapped polyline (after processing snap-to-road response).
function drawSnappedPolyline() {

    // create a new id
    var newID = 1;
    if (routeMap.size > 0) {
        // one higher than highest existing id
        newID = Math.max(...Array.from(routeMap.values()).map(p => p.id)) + 1;
    }

    displayBNOPIRoute({
        user_attrs: {},
        hidden_attrs: {},
        id: newID,
        stops: [null, null], // TODO currently routes are not tied to any stops
        links: [snappedCoordinates.map(latLng => ({
            lat: latLng.lat(),
            lon: latLng.lng()
        }))], // only 1 link.
        name: "Custom Route"
    })

    
}

function setModified() {
    modifiedStageInstance = true;
    document.getElementById("title").innerHTML = "* BNOPI *";
}

function setUnmodified() {
    modifiedStageInstance = false;
    document.getElementById("title").innerHTML = "BNOPI";
}
