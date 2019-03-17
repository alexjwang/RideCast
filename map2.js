function initMap() {
    var xmlhttp3 = new XMLHttpRequest();
    xmlhttp3.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var coordinatesArr = JSON.parse(this.responseText);
            var lti = coordinatesArr[0];
            var lgi = coordinatesArr[1];
            console.log(lti);
            for(i = 2; i < coordinatesArr.length; i++) {
                coordinatesArr[i] = JSON.parse(coordinatesArr[i]);
            }
            var map;
            var markers = new Array(coordinatesArr.length);
    
            var home = new google.maps.LatLng(
                parseFloat(lti),
                parseFloat(lgi)
            );
            map = new google.maps.Map(document.getElementById('map'), {
                center: home,
                zoom: 13
            });
    
            var myLatLngs = new Array(coordinatesArr.length);
            for(i = 2; i < coordinatesArr.length; i++) {
                myLatLngs[i] = new google.maps.LatLng(
                    parseFloat(coordinatesArr[i].lat),
                    parseFloat(coordinatesArr[i].lng)
                );
            }
    
            for(i = 2; i < coordinatesArr.length; i++) { 
                markers[i] = new google.maps.Marker({
                    position: myLatLngs[i],
                    map: map,
                })
            }
        };
      }
    
    xmlhttp3.open("GET", "http://localhost:5000/post/location", true);
    xmlhttp3.send();
    }
    