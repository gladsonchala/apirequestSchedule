import requests
import schedule
import time

def ping_api():
    api_url = "http://your-api-url/generate-response"
    params = {
        "user_message": "Keep API Active",
        "provider_name": "your_provider_name"
    }

    response = requests.post(api_url, json=params)
    if response.status_code == 200:
        return "API is kept active."
    else:
        return "Failed to keep API active."

# Define the job to run the ping_api function every 5 minutes
schedule.every(5).minutes.do(ping_api)

# Run the scheduled jobs
while True:
    schedule.run_pending()
    time.sleep(1)
