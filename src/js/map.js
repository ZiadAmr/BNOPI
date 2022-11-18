//Variable storing the google maps embedding
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

    google.maps.event.addListener(map, 'click', 
    function(event){
        if(mode == 1){
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
    fetch('https://www.overpass-api.de/api/interpreter?data=[out:json];node(around:500.0,52.4128,-1.5090)[highway=bus_stop];out;')
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
        if(mode == 2){
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
        if(mode == 2){
            busStops.get(event.latLng).setMap(null);
            busStops.delete(event.latLng);
        }
    });
}

//Called when a button from the network toolkit is clicked
function changeMode(newMode){
    //Double clicking on the same button means the user has deactivated the tool
    if(mode == newMode){
        mode = 0;
    //If clicking from a different tool active or no tool active must set the tool related to the clicked button active 
    }else{
        mode = newMode;
    }
}