"use strict";





function initMap() {
        var unitedStates = {lat: 39.8097343, lng: -98.5556199};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 4,
          center: unitedStates
        });
        var marker = new google.maps.Marker({
          position: unitedStates,
          map: map
        });
      }





























