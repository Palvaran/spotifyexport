import csv
import json
import spotipy
import time
from spotipy.oauth2 import SpotifyOAuth
from requests.exceptions import ReadTimeout

# Setup Spotify API
client_id = 'your-spotify-client-id'
client_secret = 'your-spotify-client-secret'
redirect_uri = 'your-spotify-redirect-uri'
scope = 'playlist-read-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

# Get the current user's id
current_user_id = sp.current_user()['id']

# Get user playlists
playlist_response = []
response = sp.user_playlists(current_user_id)
while response:
    playlist_response.extend(response['items'])
    if response['next']:
        response = sp.next(response)
    else:
        response = None

all_playlists = []

# For each playlist
for playlist in playlist_response:
    playlist_info = {}
    playlist_info['name'] = playlist['name']
    playlist_info['id'] = playlist['id']

    # Get tracks in the playlist
    playlist_info['tracks'] = []
    offset = 0
    while True:
        try:
            response = sp.playlist_items(playlist['id'], offset=offset)
            tracks = response['items']
        except ReadTimeout:
            print("ReadTimeout occurred, waiting for 10 seconds before retrying...")
            time.sleep(10)
            continue

        # For each track
        for item in tracks:
            if item['track'] is None:  # check if track is None
                continue  # skip to next iteration if track is None

            track_info = {}
            track_info['name'] = item['track']['name']
            track_info['id'] = item['track']['id']
            track_info['duration_ms'] = item['track']['duration_ms']

            # Check if 'popularity' key exists before accessing it
            if 'popularity' in item['track']:
                track_info['popularity'] = item['track']['popularity']
            else:
                track_info['popularity'] = None

            # Check if 'artists' key exists before accessing it
            if 'artists' in item['track']:
                track_info['artists'] = [artist['name'] for artist in item['track']['artists']]
            else:
                track_info['artists'] = None

            playlist_info['tracks'].append(track_info)

        if response['next']:
            offset += len(response['items'])
        else:
            break

    all_playlists.append(playlist_info)

# Save to a JSON file
with open(r'C:\temp\spotifyuser.json', 'w') as f:
    json.dump(all_playlists, f)

# Save to a CSV file
with open(r'C:\temp\spotifyuser.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # Write the header
    writer.writerow(['Playlist Name', 'Track Name', 'Artists', 'Duration (s)', 'Popularity'])
    # Write the data
    for playlist in all_playlists:
        for track in playlist['tracks']:
            writer.writerow([
                playlist['name'],
                track['name'],
                ', '.join(track['artists'] if track['artists'] else []),
                track['duration_ms'] / 1000,  # convert to seconds
                track['popularity']
            ])
