# my_module.py
import requests

def get_data(url):
    """Fetches content from a given URL using the requests library."""
    try:
        # Note: This old version of requests uses the old vulnerable urllib3
        response = requests.get(url, timeout=5)
        response.raise_for_status() # Raise exception for bad status codes (4xx or 5xx)
        return response.text[:50] # Return first 50 chars of text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def simple_math(a, b):
    """A simple function to ensure tests run."""
    return a + b
