import requests
function_url = "https://europe-west10-proven-cogency-421707.cloudfunctions.net/weather_api_project"

data = {"": ""}
response = requests.post(function_url, json=data)

# Check for successful response
if response.status_code == 200:
    print("POST request successful!")
    print(response.text)
    # Access the response content (optional)
    # print(response.text)
else:
    print(f"Error: {response.status_code}")
    print(response.text)
