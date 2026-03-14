import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(".env")

API_KEY = os.getenv("API_KEY")
CHANNEL_HANDLE = "@MrBeast"

def get_playlist_id():
    try:
        if not API_KEY:
            raise ValueError("API_KEY was not loaded from .env")

        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"
        
        response = requests.get(url)
        print("Status code:", response.status_code)

        data = response.json()
        print(json.dumps(data, indent=4))

        if response.status_code != 200:
            raise ValueError(f"API request failed: {data}")

        if "items" not in data or not data["items"]:
            raise ValueError("No channel items found in API response")

        channel_item = data["items"][0]
        uploads_playlist_id = channel_item["contentDetails"]["relatedPlaylists"]["uploads"]

        print("Uploads playlist ID:", uploads_playlist_id)
        return uploads_playlist_id

    except requests.exceptions.RequestException as e:
        raise e

if __name__ == "__main__":
    get_playlist_id()