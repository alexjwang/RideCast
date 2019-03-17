var mapsurl = "https://maps.googleapis.com/maps/api/staticmap?center=40.7099937,-73.9302593&zoom=10&size=500x450&markers=color:red%7Clabel:S%7C"
mapsurl += coordinates + "&key=AIzaSyDOcAauPBKu0QK8U4ItFAa1FtgtzcfO4Yo"


var image = document.getElementById("hotspotmap");
image.src = mapsurl;


// "https://maps.googleapis.com/maps/api/staticmap?center=Brooklyn+Bridge,New+York,NY&zoom=13&size=600x300&maptype=roadmap&markers=color:blue%7Clabel:S%7C40.702147,-74.015794&markers=color:green%7Clabel:G%7C40.711614,-74.012318&markers=color:red%7Clabel:C%7C40.718217,-73.998284&key=AIzaSyDOcAauPBKu0QK8U4ItFAa1FtgtzcfO4Yo"