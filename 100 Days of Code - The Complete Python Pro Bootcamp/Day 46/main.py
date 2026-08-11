import requests
import json

# ---------------------------------------------------------
# CONFIGURATION — replace these with your actual credentials
# ---------------------------------------------------------
DEVELOPER_TOKEN = "YOUR_DEVELOPER_TOKEN"
USER_TOKEN = "YOUR_USER_TOKEN"
STORE_FRONT = "us"  # or "za" for South Africa, etc.

BASE_URL = "https://api.music.apple.com/v1/me"


# ---------------------------------------------------------
# Helper: Get existing playlists
# ---------------------------------------------------------
def get_existing_playlists():
    url = f"{BASE_URL}/library/playlists"
    headers = {
        "Authorization": f"Bearer {DEVELOPER_TOKEN}",
        "Music-User-Token": USER_TOKEN
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json().get("data", [])


# ---------------------------------------------------------
# Helper: Generate playlist name with integer if needed
# ---------------------------------------------------------
def generate_playlist_name(base_name="ThisWeeksTopSongs"):
    playlists = get_existing_playlists()
    names = [p["attributes"]["name"] for p in playlists]

    if base_name not in names:
        return base_name

    # If name exists, append integer
    counter = 1
    while f"{base_name}{counter}" in names:
        counter += 1

    return f"{base_name}{counter}"


# ---------------------------------------------------------
# Fetch Top 100 songs of the week
# Apple Music chart endpoint
# ---------------------------------------------------------
def get_top_100_songs():
    url = f"https://api.music.apple.com/v1/catalog/{STORE_FRONT}/charts?types=songs&limit=100"
    headers = {
        "Authorization": f"Bearer {DEVELOPER_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    chart = response.json()["results"]["songs"][0]["data"]
    song_ids = [song["id"] for song in chart]
    return song_ids


# ---------------------------------------------------------
# Create playlist
# ---------------------------------------------------------
def create_playlist(name, song_ids):
    url = f"{BASE_URL}/library/playlists"
    headers = {
        "Authorization": f"Bearer {DEVELOPER_TOKEN}",
        "Music-User-Token": USER_TOKEN,
        "Content-Type": "application/json"
    }

    payload = {
        "attributes": {
            "name": name,
            "description": "Top 100 songs of the week automatically generated."
        },
        "relationships": {
            "tracks": {
                "data": [{"id": sid, "type": "songs"} for sid in song_ids]
            }
        }
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    response.raise_for_status()
    return response.json()


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
def main():
    print("Fetching Top 100 songs...")
    top_songs = get_top_100_songs()

    print("Generating playlist name...")
    playlist_name = generate_playlist_name()

    print(f"Creating playlist: {playlist_name}")
    result = create_playlist(playlist_name, top_songs)

    print("Playlist created successfully!")
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
