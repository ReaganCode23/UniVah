// Function to handle form submission and show ride details
function confirmRide(event) {
    event.preventDefault(); // Prevent form from submitting

    // Get form values
    const pickup = document.getElementById('pickup').value;
    const dropoff = document.getElementById('dropoff').value;
    const schedule = document.getElementById('schedule').value;
    const payment = document.getElementById('payment').value;

    // Estimate fare (simple logic for demo purposes)
    const distance = Math.floor(Math.random() * 15) + 5; // Random distance between 5-20 km
    const fare = distance * 2; // Example fare: $2 per km

    // Update ride summary
    const rideSummary = `Pickup: ${pickup}, Drop-off: ${dropoff}, Schedule: ${schedule === 'instant' ? 'Instant Ride' : 'Scheduled Ride'}, Payment: ${payment}`;
    document.getElementById('ride-summary').innerText = rideSummary;
    document.getElementById('fare').innerText = fare;

    // Show ride details
    document.getElementById('ride-details').classList.remove('hidden');
}

// Function to simulate GPS tracking
function startTracking() {
    document.getElementById('ride-map').classList.remove('hidden');
    let timeRemaining = 5;

    // Update driver location every second
    const trackingInterval = setInterval(() => {
        timeRemaining--;
        document.getElementById('driver-location').innerText = `Driver is ${timeRemaining} minutes away.`;

        if (timeRemaining === 0) {
            clearInterval(trackingInterval);
            document.getElementById('driver-location').innerText = "Driver has arrived!";
        }
    }, 1000); // Update every second (for demo purposes)
}
