import time
import requests
from requests.exceptions import ConnectionError, Timeout, HTTPError, RequestException


def safe_api_request_with_retry(url, timeout=5, retries=3):
    """API request with retry logic"""

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()

            return {"success": True, "data": response.json()}

        except (ConnectionError, Timeout, HTTPError, RequestException) as e:
            print(f"Attempt {attempt} failed: {e}")

            if attempt < retries:
                time.sleep(2)
            else:
                return {"success": False, "error": "All retry attempts failed"}


# ✅ THIS MUST BE OUTSIDE THE FUNCTION
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/todos/1"
    result = safe_api_request_with_retry(url)
    print(result)