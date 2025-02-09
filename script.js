document.getElementById('weatherForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const location = document.getElementById('location').value;
    fetchWeatherData(location);
});

function fetchWeatherData(location) {
    fetch(`/weather?location=${location}`)
        .then(response => response.json())
        .then(data => {
            const weatherData = document.getElementById('weatherData');
            let forecastHTML = `<h2>Weather Forecast for ${data.location}</h2>`;
            data.forecast.forEach(day => {
                forecastHTML += `
                    <p>Date: ${day.date}, Temperature: ${day.temperature}°C</p>
                `;
            });
            weatherData.innerHTML = forecastHTML;
        })
        .catch(error => {
            console.error('Error fetching weather data:', error);
        });
}