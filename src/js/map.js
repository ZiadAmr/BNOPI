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
    fetch('https://www.overpass-api.de/api/interpreter?data=[out:json];node(around:2100, 52.52955, -1.22395)[highway=bus_stop];out;')
        .then((response) => response.json())
        .then((data) => createStopMarkers(data));

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
