import requests
import json
import time

# The API url
url = "https://api.ecoflow.com/iot-service/open/api/device/queryDeviceQuota"

# Headers for the API request
headers = {
    'Content-Type': 'application/json',
    'appKey': 'f0a0e57338064d38abae2031f5d3d7ea',
    'secretKey': 'd828c879a1be4cfe9d3f577bb4e4656b'
}

# Device serial number
device = "DCABZ8ZE7080453"

# Get parameters for the request
params = {'sn': device}

# Loop forever
while True:
    # Make the request
    response = requests.get(url, headers=headers, params=params)

    # Check if request was successful
    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data)) # print in one line
    else:
        print(f"Request failed for device {device} with status code: {response.status_code}")

    # Wait for 5 minutes before next request
    time.sleep(300)
