





function initMap() {
        var unitedStates = {lat: 39.8097343, lng: -98.5556199};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 4,
          center: unitedStates,
          scrollwheel: false,
          disableDoubleClickZoom: true,
        });

        setMarkers(map);
      }





var locations = [['Washington DC', 38.907192, -77.036871],
                ['Seattle', 47.60621, -122.332071],
                ['San Diego', 32.715738, -117.161084],
                ['Las Vegas', 36.169941, -115.13983],
                ['Portland',45.523062, -122.676482],
                ['New York City', 40.712784, -74.005941],
                ['Los Angeles', 34.052234, -118.243685],
                ['Chicago', 41.878114, -87.629798],
                ['Boston', 42.360083, -71.05888],
                ['Miami', 25.76168, -80.19179],
                ['San Francisco', 37.77493, -122.419416]];



function setMarkers(map) {
    var image = {
    url: 'https://maps.gstatic.com/mapfiles/ms2/micons/plane.png',
    size: new google.maps.Size(20, 32),
    origin: new google.maps.Point(0, 0),
    anchor: new google.maps.Point(0, 32)
  };
  var shape = {
    coords: [1, 1, 1, 20, 18, 20, 18, 1],
    type: 'poly'
  };
  for (var i = 0; i < locations.length; i++) {
    var location = locations[i];
    var marker = new google.maps.Marker({
      position: {lat: location[1], lng: location[2]},
      map: map,
      icon: image,
      shape: shape,
      title: location[0],
    });
  }
}








// doughnut chart

var options = { responsive: true };

var ctx_donut = $("#donutChart").get(0).getContext("2d");

$.get("/origin-budget.json", function (data) {
    var myDonutChart = new Chart(ctx_donut, {
                                            type: 'doughnut',
                                            data: data,
                                            options: options
                                          });
    $('#donutLegend').html(myDonutChart.generateLegend());
});















