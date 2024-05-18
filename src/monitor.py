import time
import requests
from prometheus_client import start_http_server, Summary

# Create a metric to track time spent and requests made
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

def monitor():
    """Main monitoring function."""
    while True:
        try:
            # Simulate a request to the model server
            response = requests.get("http://localhost:5000")  # Update URL if needed
            if response.status_code == 200:
                print("Model server is up and running")
            else:
                print(f"Unexpected status code: {response.status_code}")

            # Simulate processing time for metrics
            process_request(1)
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to the model server: {e}")

        time.sleep(10)  # Wait for 10 seconds before the next check

if __name__ == "__main__":
    # Start up the server to expose the metrics
    start_http_server(8000)
    print("Starting monitoring on port 8000")
    monitor()
