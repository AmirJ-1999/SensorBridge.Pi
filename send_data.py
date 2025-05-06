import requests
from datetime import datetime

# Definer URL til API-endepunktet
url = "http://localhost:5000/api/plantlog" 

# Eksempeldata (du kan ændre værdierne)
data = {
    "Plant_ID": 1,
    "TemperatureLevel": 22.8,
    "LightLevel": 350.0,
    "WaterLevel": 40.5,
    "AirHumidityLevel": 65.2
}

# Send POST-request
response = requests.post(url, json=data)

# Print svar
print("Statuskode:", response.status_code) 
print("Svar:", response.text)

