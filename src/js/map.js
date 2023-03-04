//Variable storing the google maps embedding
var map;

//Code used for polylines (drawing a route on the map was directly referenced from google maps documentation)
//https://developers.google.com/maps/documentation/roads/snap
var apiKey = 'AIzaSyAWmWHoyHgni9A2p4kYBloFIuTeE4linzo';
var drawingManager;
var snappedCoordinates = [];
var polyMap = new Map();

//Elements relating to editing a polyline
var selectedPolyline = null;    //When a user clicks on another polyline after editing one (instead of clicking save), this variable will be used to change the setting to editable = false

//Code for styling the map
var styleArray = [
  {featureType: "poi", stylers: [{ visibility: "off" }]},
  {featureType: "transit", stylers: [{ visibility: "on" }]}
];

function initMap(){
    var optionParams = {
        zoom:14,
        center:{lat:52.52955,lng:-1.22395},
        mapTypeId: "terrain"
    };

    map = new google.maps.Map(document.getElementById('map'), optionParams);
    //Ensures the map only displays roads
    map.setOptions({styles: styleArray});

    google.maps.event.addListener(map, 'click', 
    function(event){
        if(window.localStorage.getItem('mode') == 1){
            createGoogleMarker(event);
        }
    });

    // var request = {
    //     location: {lat:52.4128,lng:-1.5090},
    //     radius: '500',
    //     rankby: "distance",
    //     type: ["bus_station"]
    // };

    //Getting the bus stop location data using openstreetmap api
    // fetch('https://www.overpass-api.de/api/interpreter?data=[out:json];node(around:2100, 52.52955, -1.22395)[highway=bus_stop];out;')
    //     .then((response) => response.json())
    //     .then((data) => createStopMarkers(data));


    // get the stage format stop file
    var broughtonStopsStgFmt = { stops: [{ name: "Warwick Road", id: 562724487, lat: 52.5386566, lon: -1.2370591 }, { name: "Warwick Road", id: 562724490, lat: 52.5387703, lon: -1.2365706 }, { name: "Leicester Road", id: 562724491, lat: 52.5386246, lon: -1.2335063 }, { name: "Leicester Road", id: 562724493, lat: 52.5385261, lon: -1.232181 }, { name: "Peregrine Road", id: 562724495, lat: 52.5377247, lon: -1.2292167 }, { name: "Condor Close", id: 562724498, lat: 52.5361496, lon: -1.2261923 }, { name: "Byre Crescent", id: 562724499, lat: 52.5260033, lon: -1.2185583 }, { name: "Byre Crescent", id: 562724501, lat: 52.5258834, lon: -1.2181035 }, { name: "Byre Crescent", id: 562724503, lat: 52.525166, lon: -1.2170107 }, { name: "Red Admiral PH", id: 562724504, lat: 52.5240478, lon: -1.2137879 }, { name: "Red Admiral PH", id: 562724507, lat: 52.5238472, lon: -1.213364 }, { name: "Orchard Place", id: 562724509, lat: 52.5222012, lon: -1.2105488 }, { name: "Orchard Place", id: 562724510, lat: 52.5217333, lon: -1.2104983 }, { name: "Old Mill Road", id: 562724512, lat: 52.5280303, lon: -1.2205566 }, { name: "Station Road", id: 562724513, lat: 52.5286564, lon: -1.22143 }, { name: "The White Horse Inn PH", id: 562724516, lat: 52.5295293, lon: -1.2242891 }, { name: "The White Horse Inn PH", id: 562724518, lat: 52.5295913, lon: -1.2241553 }, { name: "The Old Bulls Head PH", id: 562724519, lat: 52.5312288, lon: -1.2270896 }, { name: "Broughton House", id: 562724521, lat: 52.5314726, lon: -1.2272475 }, { name: "School Crescent", id: 562724523, lat: 52.532766, lon: -1.2284484 }, { name: "Main Street Post Office", id: 562724525, lat: 52.5330126, lon: -1.2290338 }, { name: "Main Street", id: 562724527, lat: 52.5337951, lon: -1.2304796 }, { name: "Main Street", id: 562724528, lat: 52.53399, lon: -1.2314198 }, { name: "Blenheim Crescent", id: 562724530, lat: 52.5364654, lon: -1.2360503 }, { name: "Blenheim Crescent", id: 562724531, lat: 52.5359664, lon: -1.2339654 }, { name: "Broughton Way", id: 562724533, lat: 52.5293123, lon: -1.2186323 }, { name: "Holbeck Drive", id: 562724536, lat: 52.5280087, lon: -1.2145574 }, { name: "Lea Close", id: 562724538, lat: 52.5256566, lon: -1.2123589 }, { name: "Red Admiral PH", id: 562724543, lat: 52.5243674, lon: -1.2131779 }, { name: "Peregrine Road", id: 562724546, lat: 52.5376084, lon: -1.2293072 }, { name: "The Fieldway", id: 562724548, lat: 52.5264411, lon: -1.2208648 }, { name: "Lea Close", id: 562724550, lat: 52.5253713, lon: -1.2127177 }, { name: "Holbeck Drive", id: 562724552, lat: 52.5276486, lon: -1.2144901 }] };
    createMarkersFromStageFormat(broughtonStopsStgFmt);

    // check that we can convert the stops to json
    console.log(stopsToJson());
    

    //Code used for using google maps api to get the bus stop location data
    //var service = new google.maps.places.PlacesService(map);
    //service.nearbySearch(request, placeStops)
}

// function placeStops(results, status){
//     if(status == google.maps.places.PlacesServiceStatus.OK){
//         console.log(results)
//         for (var i = 0; i < results.length; i++){
//             createGoogleMarker(results[i]);
//         }
//     }
// }

function createStopMarkers(results){
    console.log(results.elements.length + " Bus stops loaded");
    for(var i = 0; i < results.elements.length; i++){
        createMarker(results.elements[i])
    }
}

//Called when a marker is created by clicking on the map
function createGoogleMarker(marker){
    temp = new google.maps.Marker({
        position: marker.latLng,
        map: map,
        title: "Bus stop",
        icon: {
           size: new google.maps.Size(50, 50),
           scaledSize: new google.maps.Size(50, 50),
           url: "icons/bus-station.png"
        }
    })
    busStops.set(temp.position, temp);
    google.maps.event.addListener(temp, 'click', function deleteMarker(event) {
        
        //The user has clicked the delete markers button 
        if(window.localStorage.getItem('mode') == 2){
            busStops.get(event.latLng).setMap(null);
            busStops.delete(event.latLng);
        }
    });

}

function createMarker(marker){
    var position = {lat:marker.lat, lng:marker.lon}
    temp = new google.maps.Marker({
        position: position,
        map,
        title: "Bus stop",
        icon: {
            size: new google.maps.Size(50, 50),
            scaledSize: new google.maps.Size(50, 50),
            url: "icons/bus-station.png"
        }
    })
    busStops.set(temp.position, temp);
    google.maps.event.addListener(temp, 'click', function deleteMarker(event) {
        
        //The user has clicked the delete markers button 
        if(window.localStorage.getItem('mode') == 2){
            busStops.get(event.latLng).setMap(null);
            busStops.delete(event.latLng);
        }
    });
}

/**
 * 
 * @param {Object} jsonData Parsed json from the stops stage format
 */
function createMarkersFromStageFormat(jsonData) {
    jsonData.stops.forEach(stop => {

        // create google maps marker.
        // keep the stop id for now in case it needs to be assigned a new id,
        // but note that the id will be reassigned when the stop stage instance is exported
        const position = {lat:stop.lat, lng:stop.lon};
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

function stopsToJson() {

    var id_counter = 0;

    var stops = [];

    for (let stop of busStops.values()) {
        
        var lat = stop.position.lat;
        var lon = stop.position.lon;
        var name = "";
        if (stop.name != undefined){
            name = stop.name;
        }
        var id = id_counter++;

        stops.push({
            "lat": lat,
            "lon": lon,
            "name": name,
            "id":id
        });
        
    }

    return {"stops":stops};
}

//Called when a button from the network toolkit is clicked
function changeMode(newMode){
    //If the last mode the program was in was add route mode, we need to disable the drawing manager
    if(window.localStorage.getItem('mode') == 3){
        disableRouteDraw();
    }else if (window.localStorage.getItem('mode') == 5){

        if (selectedPolyline!= null){
            selectedPolyline.setOptions({editable:false});
            selectedPolyline = null;
        }
    }

    //Double clicking on the same button means the user has deactivated the tool
    if(window.localStorage.getItem('mode') == newMode){
        window.localStorage.setItem('mode', 0);
    //If clicking from a different tool active or no tool active must set the tool related to the clicked button active 
    }else{
        window.localStorage.setItem('mode',newMode);
    }

    //If the new mode is 3 we need to start the drawing manager
    if(window.localStorage.getItem('mode') == 3){
        enableRouteDraw();
    }
}


//This code is part of google maps stick to road documentation (include that in the report references)
//Once the draw a route button is clicked, this function will be called
function enableRouteDraw(){
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
    drawingManager.addListener('polylinecomplete', function(poly) {
        var path = poly.getPath();
        poly.setMap(null);
        runSnapToRoad(path);
    });
}

function disableRouteDraw(){
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
    }, function(data) {
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
    polyMap.set(count,snappedPolyline);
    snappedPolyline.addListener('click',function deleteRoute(){
        if(window.localStorage.getItem('mode') == 4){
            //Remember to remove it from the list of polylines as well
            snappedPolyline.setMap(null);
            //Remove the polyline from the list
            polyMap.delete(count);
        }else if(window.localStorage.getItem('mode') == 5){
            this.setOptions({editable: true});

            //If the user had clicked on another polyline before (make that previous polyline uneditable)
            if(selectedPolyline != null){
                selectedPolyline.setOptions({editable:false});
            }
            selectedPolyline = this;
        }
    })
}
