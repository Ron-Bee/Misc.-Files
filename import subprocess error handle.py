import subprocess
import os
import requests  # You'll need to install the requests library: pip install requests

def invoke_web_request(url, outfile):
    """Downloads a file from the given URL and saves it to the specified outfile.

    Args:
        url (str): The URL of the file to download.
        outfile (str): The path where the downloaded file should be saved.

    Raises:
        requests.exceptions.RequestException: For general request errors.
        requests.exceptions.Timeout: If the request times out.
        requests.exceptions.HTTPError: For HTTP errors (e.g., 401 Unauthorized)
    """

    os.makedirs(os.path.dirname(outfile), exist_ok=True)

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for error status codes

        with open(outfile, 'wb') as f:
            f.write(response.content)

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
    except requests.exceptions.Timeout as e:
        print(f"Request to {url} timed out: {e}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error for {url}: {e.response.status_code} - {e.response.text}")

# ... (rest of the script remains the same) 