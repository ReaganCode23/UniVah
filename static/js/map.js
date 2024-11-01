function initializeMap() {
    // Initialize map
    var map = L.map('map').setView([37.7749, -122.4194], 13);
    
    // Add OpenStreetMap tile layer
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Function to display route
    function displayRoute() {
        var pickupAddress = document.getElementById('pickup');
        var dropoffAddress = document.getElementById('dropoff');
        
        // Create geocoder instance
        var geocoder = L.Control.Geocoder.nominatim();
        
        // Geocode pickup address
        geocoder.geocode(pickupAddress, function(pickupResults) {
            if (pickupResults.length > 0) {
                var pickupLatLng = pickupResults[0].center;
                
                // Geocode dropoff address
                geocoder.geocode(dropoffAddress, function(dropoffResults) {
                    if (dropoffResults.length > 0) {
                        var dropoffLatLng = dropoffResults[0].center;
                        
                        // Clear previous route (if any)
                        if (window.routeControl) {
                            map.removeControl(window.routeControl);
                        }
                        
                        // Display route between pickup and dropoff locations
                        window.routeControl = L.Routing.control({
                            waypoints: [
                                L.latLng(pickupLatLng),
                                L.latLng(dropoffLatLng)
                            ],
                            routeWhileDragging: true,
                            createMarker: function(i, waypoint) {
                                var markerIcon = L.divIcon({
                                    className: 'custom-marker',
                                    html: i === 0 ? '🏁' : '🏠',
                                    iconSize: [30, 30]
                                });
                                return L.marker(waypoint.latLng, { icon: markerIcon });
                            }
                        }).addTo(map);
                        
                        // Fit map to show entire route
                        map.fitBounds([pickupLatLng, dropoffLatLng]);
                    } else {
                        alert("Dropoff location not found.");
                    }
                });
            } else {
                alert("Pickup location not found.");
            }
        });
    }

    // Add event listener to display route when form is submitted
    document.getElementById('ride-form').addEventListener('submit', function(event) {
        event.preventDefault();
        displayRoute();
    });
}

// Call initializeMap when the page loads
window.onload = initializeMap;
