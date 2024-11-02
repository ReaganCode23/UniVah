// Initialize the map
var map = L.map('map').setView([51.505, -0.09], 13);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Initialize the geocoder
var geocoder = L.Control.Geocoder.nominatim();

var rideData = document.getElementById("ride-data");
var pickupAddress = rideData.getAttribute("data-pickup");
var dropoffAddress = rideData.getAttribute("data-dropoff");
// Check the pickup and dropoff addresses
console.log("Pickup Address:", pickupAddress);
console.log("Dropoff Address:", dropoffAddress);

// Geocode the pickup location
geocoder.geocode(pickupAddress, function(pickupResults) {
    if (pickupResults && pickupResults.length > 0) {
        var pickupLatLng = pickupResults[0].center;
        L.marker(pickupLatLng).addTo(map).bindPopup("Pickup Location").openPopup();

        // Geocode the dropoff location
        geocoder.geocode(dropoffAddress, function(dropoffResults) {
            if (dropoffResults && dropoffResults.length > 0) {
                var dropoffLatLng = dropoffResults[0].center;
                L.marker(dropoffLatLng).addTo(map).bindPopup("Dropoff Location");

                // Calculate and display the route using OSRM
                var osrmUrl = `https://router.project-osrm.org/route/v1/driving/${pickupLatLng.lng},${pickupLatLng.lat};${dropoffLatLng.lng},${dropoffLatLng.lat}?overview=full&geometries=geojson`;

                fetch(osrmUrl)
                    .then(response => response.json())
                    .then(data => {
                        if (data.routes && data.routes.length > 0) {
                            var routeCoordinates = data.routes[0].geometry.coordinates.map(coord => [coord[1], coord[0]]);
                            var route = L.polyline(routeCoordinates, { color: 'blue' }).addTo(map);
                            map.fitBounds(route.getBounds());
                        } else {
                            console.error('Route not found in OSRM response:', data);
                            alert('Route not found');
                        }
                    })
                    .catch(error => {
                        console.error('Error fetching route:', error);
                        alert('Failed to calculate route');
                    });
            } else {
                console.error('Dropoff location geocoding failed:', dropoffResults);
                alert('Dropoff location not found');
            }
        });
    } else {
        console.error('Pickup location geocoding failed:', pickupResults);
        alert('Pickup location not found');
    }
});
