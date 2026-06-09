import logging
import requests

# 🔧 setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def logged_api_request(url):
    logging.info(f"Requesting URL: {url}")

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        logging.info("Request successful")
        return response.json()

    except Exception as e:
        logging.error(f"Request failed: {e}")
        return None

url = "https://jsonplaceholder.typicode.com/todos/1"

result = logged_api_request(url)

print("OUTPUT:")
print(result)