import requests
import os
from urllib.parse import urlparse

def fetch_image(url):
    """
    Fetches an image from the given URL and saves it to Fetched_Images directory.
    Returns the filepath if successful, None otherwise.
    """
    try:
        os.makedirs("Fetched_Images", exist_ok=True)

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Verify it's an image
        if "image" not in response.headers.get("Content-Type", ""):
            print(f"✗ Skipped (not an image): {url}")
            return None

        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path) or "downloaded_image.jpg"
        filepath = os.path.join("Fetched_Images", filename)

        if os.path.exists(filepath):
            print(f"✗ Skipping duplicate: {filename}")
            return None

        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")
        return filepath

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error: {e}")
    except Exception as e:
        print(f"✗ An error occurred: {e}")
    return None


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    urls = input("Please enter image URLs (comma-separated): ").split(",")

    for url in [u.strip() for u in urls if u.strip()]:
        fetch_image(url)

    print("\nConnection strengthened. Community enriched.")
    print("Ubuntu: 'I am because we are.'")


if __name__ == "__main__":
    main()
