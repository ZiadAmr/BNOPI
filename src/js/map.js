//Variable storing the google maps embedding
var map;

//Code used for polylines (drawing a route on the map was directly referenced from google maps documentation)
//https://developers.google.com/maps/documentation/roads/snap
var apiKey = 'AIzaSyAWmWHoyHgni9A2p4kYBloFIuTeE4linzo';
var drawingManager;
var snappedCoordinates = [];


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

    google.maps.event.addListener(map, 'click',
        function (event) {
            if (window.localStorage.getItem('mode') == 1) {
                createGoogleMarker(event);
            }
        });

    //route_network_display_framework("/Users/danuk/Desktop/BNOPI/projects/test_project/stage_instances/temp.stg.json", "/Users/danuk/Desktop/BNOPI/projects/test_project/stage_instances/stop_connection.stg.json")
    route_network_display_framework("E:/BNOPI/projects/test_project/stage_instances/temp.stg.json", "E:/BNOPI/projects/test_project/stage_instances/stop_connection.stg.json")


    // add open project event listener
    window.electron.onOpenProject((_event, projPath) => openProject(projPath));
}

async function openProject(projPath) {
    // save and close any prject that might already be open TODO.

    // add this project to the recents
    await window.electron.addToRecents(projPath);

    // get the project metadata
    const projMetadata = await window.electron.getProjectMetadata(projPath);
    
    // get list of stage instances
    const stageInstances = await window.electron.getListOfStageFormat(projPath);
    
    // get dependency graph (not implemented)
    // TODO


    // actually display this stuff
    // clear the stage tracker and add the list of stages to it
    // TODO

    console.log(stageInstances)
    console.log(projMetadata);

    // TODO hard code it to open one of the stage instances
    // look for a file named STOPS_1.
    const re = /STOPS_1/;
    const stopsInstance = stageInstances.find((ins) => ins.path.match(re) != null);
    displayStageInstance(stopsInstance.path);

    return null;


}

async function displayStageInstance(instanceMetdataPath, requirementMetadataPaths) {

    // save the currently open stage instance TODO!

    // clear any stage instance already diplaying
    busStops.forEach(stop => {
        stop.setMap(null);
    });
    busStops.clear();


    /* clear routes as well TODO */
    
    const {stops, routes} = await window.electron.loadStageInstance(instanceMetdataPath, requirementMetadataPaths);

    for (const stop of stops) {
        displayBNOPIStop(stop);
    }

    // TODO display route



}


/** Display a bus stop from the BNOPI format (that which is received from the stage format handler).
 * Converts the stop into a google maps marker.
 * 
 * @param {{lat: number; lon: number; id: number; name: string | undefined; hidden_attrs: any; user_attrs: any;}} stop Stop in BNOPI format
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
            busStops.get(event.latLng).setMap(null);
            busStops.delete(event.latLng);
            window.dispatchEvent(new Event('bus_stops_change'));
        }
    });

}

/**
 * Display a route from the BNOPI format (that which is received from the stage format handler).
 * 
 * @param {{id: number; name: string | undefined; points: {lat: number; lon: number;}[]; hidden_attrs: any; user_attrs: any;}} route Route in BNOPI format
 */
function displayBNOPIRoute(route) {

}

function createStopMarkers(results) {
    console.log(results.elements.length + " Bus stops loaded");
    for (var i = 0; i < results.elements.length; i++) {
        createMarker(results.elements[i])
    }
}

//Called when a marker is created by clicking on the map
function createGoogleMarker(marker) {
    temp = new google.maps.Marker({
        position: marker.latLng,
        map: map,
        title: "Bus stop",
        name: "Custom stop",
        icon: {
            size: new google.maps.Size(30, 30),
            scaledSize: new google.maps.Size(30, 30),
            url: "icons/bus-station.png"
        }
    })
    busStops.set(temp.position, temp);
    google.maps.event.addListener(temp, 'click', function deleteMarker(event) {

        //The user has clicked the delete markers button 
        if (window.localStorage.getItem('mode') == 2) {
            busStops.get(event.latLng).setMap(null);
            busStops.delete(event.latLng);
            window.dispatchEvent(new Event('bus_stops_change'));
        }
    });
    window.dispatchEvent(new Event('bus_stops_change'));
}

/** 
 * @deprecated Instead bus stop markers are read from a file using a display framework. Then the function displayStageInstance in map.js is called, which within calls displayBNOPIStop.
 * @param {Object} jsonData Parsed json from the stops stage format
 */
function createMarkersFromStageFormat(jsonData) {
    jsonData.stops.forEach(stop => {

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
                size: new google.maps.Size(30, 30),
                scaledSize: new google.maps.Size(30, 30),
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
                window.dispatchEvent(new Event('bus_stops_change'));
            }
        });

    });
    window.dispatchEvent(new Event('bus_stops_change'));
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

/**
 * Note these are both metadata locations
 * @param {String} network_path Path to the network to be displayed
 * @param {String} dependency_graph_path Path to the dependency_graph 
 */
async function route_network_display_framework(network_path, dependency_graph_path){
    const points_map = new Map();
    const links_map = new Map();

    const decoder = new TextDecoder('utf-8')

    // Read the dependency graph
    const stp_conn = await window.electron.openStageFormat("temp", "stp", dependency_graph_path)
    const stp = JSON.parse(decoder.decode(stp_conn.data))

    // Read the generated network
    const network = await window.electron.openStageFormat("temp", "network", network_path)
    const netw = JSON.parse(decoder.decode(network.data))

    // Create a Map object from the points
    for (let i = 0; i < stp.points.length; i++){
        points_map.set(stp.points[i].id, stp.points[i])
    }

    for (let i = 0; i <stp.links.length; i++){
        links_map.set(stp.links[i].id, stp.links[i])
    }

    for(let i = 0; i < netw.routes.length;i++){
        // List containing the points which needs to be drawn to display the route
        poly_points = []
        for(let j = 0; j < netw.routes[i].links.length; j++){
            points = links_map.get(netw.routes[i].links[j]).points
            for(let k = 0; k < points.length; k++){
                current_point = points_map.get(points[k])
                var latlng = new google.maps.LatLng(
                    current_point.lat,
                    current_point.lon
                )
                poly_points.push(latlng)
            }
        }
        const color = "#" + Math.floor(Math.random() * 16777215).toString(16);
        routes = new google.maps.Polyline({
            path: poly_points,
            strokeColor: color,
            strokeWeight: 8,
            strokeOpacity: 1,
        });
        routes.setMap(map);

        var count = +window.localStorage.getItem('routeCounter') + 1;
        //Update the localstoreage
        window.localStorage.setItem("routeCounter", count);
        polyMap.set(count, routes);

        (function(){
            let local_count = count;
            routes.addListener('click', function() {
                console.log(local_count)
                if (window.localStorage.getItem('mode') == 4) {
                    //Remember to remove it from the list of polylines as well
                    this.setMap(null);
                    //routes.setMap(null);
                    //Remove the polyline from the list
                    polyMap.delete(local_count);
                    console.log(polyMap)
                } else if (window.localStorage.getItem('mode') == 5) {
                    this.setOptions({ editable: true });
    
                    //If the user had clicked on another polyline before (make that previous polyline uneditable)
                    if (selectedPolyline != null) {
                        selectedPolyline.setOptions({ editable: false });
                    }
                    selectedPolyline = this;
                }
            })
        })()
    }
    
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


//This code is part of google maps stick to road documentation (include that in the report references)
//Once the draw a route button is clicked, this function will be called
function enableRouteDraw() {
    // Enables the polyline drawing control. Click on the map to start drawing a
    // polyline. Each click will add a new vertice. Double-click to stop drawing.
    drawingManager = new google.maps.drawing.DrawingManager({
        drawingMode: google.maps.drawing.OverlayType.POLYLINE,
        drawingControl: true,
        drawingControlOptions: {
            position: google.maps.ControlPosition.TOP_CENTER,
            drawingModes: [
                google.maps.drawing.OverlayType.POLYLINE
            ]
        },
        polylineOptions: {
            strokeColor: '#696969',
            strokeWeight: 4,
            strokeOpacity: 1,
        }
    });
    drawingManager.setMap(map);

    // Snap-to-road when the polyline is completed.
    drawingManager.addListener('polylinecomplete', function (poly) {
        var path = poly.getPath();
        poly.setMap(null);
        runSnapToRoad(path);
    });
}

function disableRouteDraw() {
    drawingManager.setMap(null);
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
    var snappedPolyline = new google.maps.Polyline({
        path: snappedCoordinates,
        strokeColor: '#00FF00',
        strokeWeight: 5,
        strokeOpacity: 1,
    });

    snappedPolyline.setMap(map);
    var count = +window.localStorage.getItem('routeCounter') + 1;
    //Update the localstoreage
    window.localStorage.setItem("routeCounter", count);
    polyMap.set(count, snappedPolyline);

    (function(){
        let local_count = count
        snappedPolyline.addListener('click', function() {
            console.log(local_count)
            if (window.localStorage.getItem('mode') == 4) {
                //Remember to remove it from the list of polylines as well
                this.setMap(null);
                //Remove the polyline from the list
                polyMap.delete(local_count);
                console.log(polyMap)
            } else if (window.localStorage.getItem('mode') == 5) {
                this.setOptions({ editable: true });
    
                //If the user had clicked on another polyline before (make that previous polyline uneditable)
                if (selectedPolyline != null) {
                    selectedPolyline.setOptions({ editable: false });
                }
                selectedPolyline = this;
            }
        })
    })()
}
