var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var coordinatesArr = JSON.parse(this.responseText) 
        console.log(coordinatesArr);
        var coordinates = ""
        for(i = 0; i < coordinatesArr.length; i++) {
            coordinates += "&markers=color:red%7Csize:tiny%7C" + coordinatesArr[i];
        }
        
        var mapsurl = "https://maps.googleapis.com/maps/api/staticmap?center=40.7199937,-73.9502593&zoom=10&size=600x350&scale=2"
        mapsurl += coordinates + "&key=AIzaSyDOcAauPBKu0QK8U4ItFAa1FtgtzcfO4Yo"
        
        var image = document.getElementById("hotspotmap");
        image.src = mapsurl;
    };
  }

xmlhttp.open("GET", "http://localhost:5000/get/hotspots", true);
xmlhttp.send();




// "https://maps.googleapis.com/maps/api/staticmap?center=Brooklyn+Bridge,New+York,NY&zoom=13&size=600x300&maptype=roadmap&markers=color:blue%7Clabel:S%7C40.702147,-74.015794&markers=color:green%7Clabel:G%7C40.711614,-74.012318&markers=color:red%7Clabel:C%7C40.718217,-73.998284&key=AIzaSyDOcAauPBKu0QK8U4ItFAa1FtgtzcfO4Yo"