var map;
var marker = new Array()
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 40.7099937, lng: -73.9302593},
        zoom: 12
    });

    var marker = new google.maps.Marker({
        position: {lat: 40.7099937, lng: -73.9302593},
        map: map
      });
    
    var marker2 = new google.maps.Marker({
    position: {lat: 40.7099937, lng: -73.9302593},
    map: map
    });
}