import requests
import json
import time
from datetime import datetime

# The API url
url = "https://api.ecoflow.com/iot-service/open/api/device/queryDeviceQuota"

# Headers for the API request
headers = {
    'Content-Type': 'application/json',
    'appKey': 'f0a0e57338064d38abae2031f5d3d7ea',
    'secretKey': 'd828c879a1be4cfe9d3f577bb4e4656b'
}

# Device serial numbers (add your second device serial number here)
devices = ["DCABZ8ZF1140068", "DCABZ8ZE7080453"]

# Loop forever
while True:
    for device in devices:
        # Get parameters for the request
        params = {'sn': device}

        # Make the request
        response = requests.get(url, headers=headers, params=params)

        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            print(f"Data for device {device}:")
            print(json.dumps(data))  # print in one line
        else:
            print(f"Request failed for device {device} with status code: {response.status_code}")

        # Wait for 1 minute before next request for another device
        time.sleep(3)

    # Get the current date and time
    current_datetime = datetime.now()

    # Format and print the current date and time
    print("Current Date and Time:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"),"================================================================================")

    # Wait for 4 minutes before next loop iteration (total 5 minutes for each device)
    time.sleep(297)

