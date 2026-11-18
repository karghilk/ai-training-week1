import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv


# Find files relative to this Python script.
PROJECT_FOLDER = Path(__file__).resolve().parent

# Load variables from .env.
load_dotenv(PROJECT_FOLDER / ".env")
api_key = os.getenv("API_KEY")


def read_headers():
    """Send the API key, read nested JSON, and save the result."""
    if not api_key:
        print("API_KEY is missing. Check your .env file.")
        return

    try:
        response = requests.get(
            "https://httpbin.org/headers",
            headers={"X-API-Key": api_key},
            timeout=5,
        )
        response.raise_for_status()

        # Example response:
        # {"headers": {"X-Api-Key": "demo-key-123", ...}}
        data = response.json()

        # .get() supplies a default if "headers" is missing.
        received_headers = data.get("headers", {})

        # HTTP header names are case-insensitive.
        normalized_headers = {
            name.lower(): value
            for name, value in received_headers.items()
        }
        received_key = normalized_headers.get("x-api-key", "Not found")

        print(f"Server received key: {received_key}")

        result = {
            "server_received_key": received_key
        }

        with open(
            PROJECT_FOLDER / "result.json", "w", encoding="utf-8"
        ) as file:
            json.dump(result, file, indent=2)

    except requests.exceptions.Timeout:
        print("Timeout after 5 seconds: please try again")

    except requests.exceptions.ConnectionError:
        print("Connection failed: check your internet connection")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP error: {error.response.status_code}")

    except requests.exceptions.JSONDecodeError:
        print("The server did not return valid JSON")


def demonstrate_timeout():
    """Request a 10-second delay with a 3-second timeout."""
    try:
        response = requests.get(
            "https://httpbin.org/delay/10",
            timeout=3,
        )
        response.raise_for_status()
        print("The delay request completed before the timeout")

    except requests.exceptions.Timeout:
        print("Timeout after 3 seconds: please try again")

    except requests.exceptions.ConnectionError:
        print("Connection failed: check your internet connection")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP error: {error.response.status_code}")


def demonstrate_server_error():
    """Handle the HTTP 500 status using raise_for_status()."""
    try:
        response = requests.get(
            "https://httpbin.org/status/500",
            timeout=5,
        )
        response.raise_for_status()

    except requests.exceptions.HTTPError as error:
        status_code = error.response.status_code

        if status_code == 500:
            print("Server error 500 handled")
        else:
            print(f"HTTP error: {status_code}")

    except requests.exceptions.Timeout:
        print("Timeout after 5 seconds: please try again")

    except requests.exceptions.ConnectionError:
        print("Connection failed: check your internet connection")
def safe_get(url):
    """Make one initial attempt, then up to 3 retries on timeout."""
    max_retries = 3

    for attempt in range(max_retries + 1):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response

        except requests.exceptions.Timeout:
            if attempt < max_retries:
                print(f"Request timed out. Retry {attempt + 1}/3...")
            else:
                print("Request timed out after 4 attempts. Giving up.")
                return None

        except requests.exceptions.ConnectionError:
            print("Connection failed: check your internet connection")
            return None

        except requests.exceptions.HTTPError as error:
            print(f"HTTP error: {error.response.status_code}")
            return None


if __name__ == "__main__":
    read_headers()
    demonstrate_timeout()
    demonstrate_server_error()



    print("Testing safe_get:")
    response = safe_get("https://httpbin.org/delay/10")

    if response is not None:
        print("Request succeeded")