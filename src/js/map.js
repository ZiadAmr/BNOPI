var map;

//Code for styling the map
var styleArray = [
  {featureType: "poi", stylers: [{ visibility: "off" }]},
  {featureType: "transit", stylers: [{ visibility: "on" }]}
];


function initMap(){
    var optionParams = {
        zoom:14,
        center:{lat:52.4128,lng:-1.5090},
        mapTypeId: "terrain"
    };

    map = new google.maps.Map(document.getElementById('map'), optionParams);
    //Ensures the map only displays roads
    map.setOptions({styles: styleArray});

    var request = {
        location: {lat:52.4128,lng:-1.5090},
        radius: '500',
        rankby: "distance",
        type: ["bus_station"]
    };

    //Getting the bus stop location data using openstreetmap api
    fetch('https://www.overpass-api.de/api/interpreter?data=[out:json];node(around:500.0,52.4766,-1.4243)[highway=bus_stop];out;')
        .then((response) => response.json())
        .then((data) => createStopMarkers(data));

    //Code used for using google maps api to get the bus stop location data
    //var service = new google.maps.places.PlacesService(map);
    //service.nearbySearch(request, placeStops)
}

function placeStops(results, status){
    if(status == google.maps.places.PlacesServiceStatus.OK){
        console.log(results)
        for (var i = 0; i < results.length; i++){
            createGoogleMarker(results[i]);
        }
    }
}

function createStopMarkers(results){
    console.log(results.elements.length);
    for(var i = 0; i < results.elements.length; i++){
        createMarker(results.elements[i])
        console.log(results.elements[i])
    }
}

function createGoogleMarker(marker){
    new google.maps.Marker({
        position: marker.geometry.location,
        map,
        title: "Bus stop"
    })
}

function createMarker(marker){
    var position = {lat:marker.lat, lng:marker.lon}
    new google.maps.Marker({
        position: position,
        map,
        title: "Bus stop"
    })
}