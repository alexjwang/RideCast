function initMap() {
var xmlhttp2 = new XMLHttpRequest();
xmlhttp2.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var coordinatesArr = JSON.parse(this.responseText);
        for(i = 0; i < coordinatesArr.length; i++) {
            coordinatesArr[i] = JSON.parse(coordinatesArr[i]);
        }
        var map;
        var markers = new Array(coordinatesArr.length);

        map = new google.maps.Map(document.getElementById('map'), {
            center: {lat: 40.7099937, lng: -73.9302593},
            zoom: 11
        });

        var myLatLngs = new Array(coordinatesArr.length);
        for(i = 0; i < coordinatesArr.length; i++) {
            myLatLngs[i] = new google.maps.LatLng(
                parseFloat(coordinatesArr[i].lat),
                parseFloat(coordinatesArr[i].lng)
            );
        }

        for(i = 0; i < coordinatesArr.length; i++) { 
            markers[i] = new google.maps.Marker({
                position: myLatLngs[i],
                map: map,
            })
        }
    };
  }

xmlhttp2.open("GET", "http://localhost:5000/get/nearby", true);
xmlhttp2.send();
}
