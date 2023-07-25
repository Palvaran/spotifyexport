import json
import csv
import time
import spotipy
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
csv_data = []

# For each playlist
for playlist in playlist_response:
    print(f"Processing playlist {playlist['name']}...")
    playlist_info = {}
    playlist_info['name'] = playlist['name']
    playlist_info['id'] = playlist['id']

    print("Fetching tracks for the playlist...")
    tracks = sp.playlist_items(playlist['id'], additional_types=['track'])

    playlist_info['tracks'] = []

    # For each track
    for i, item in enumerate(tracks['items'], start=1):
        if item['track'] is None:  # check if track is None
            continue  # skip to next iteration if track is None

        print(f"Processing track {i} of {tracks['total']}...")

        track_info = {}
        track_info['name'] = item['track']['name']
        track_info['artists'] = [artist['name'] for artist in item['track']['artists']]
        track_info['album'] = item['track']['album']['name']
        track_info['release_date'] = item['track']['album']['release_date']  # add release date
        track_info['duration_ms'] = item['track']['duration_ms'] / 1000
        track_info['popularity'] = item['track']['popularity']

        if item['track']['id']:  # Check if track id is not None
            audio_features = sp.audio_features([item['track']['id']])  # Fetch audio features for the track
            if audio_features and audio_features[0]:  # If audio features are found
                for key in audio_features[0]:  # For each audio feature
                    track_info[key] = audio_features[0][key]  # Add audio feature to track info

        # Add track info to playlist info
        playlist_info['tracks'].append(track_info)

        # Prepare row for csv_data
        csv_row = {
            'playlist_name': playlist['name'],
            'track_name': track_info['name'],
            'artist_name': ', '.join(track_info['artists']),
            'album_name': track_info['album'],
            'release_date': track_info['release_date'],  # add release date to CSV
            'duration_s': track_info['duration_ms'],
            'popularity': track_info['popularity'],
        }
        # Add audio features to csv_row
        for key in track_info:
            if key not in csv_row:  # Skip keys that are already in csv_row
                csv_row[key] = track_info[key]

        # Add row to csv_data
        csv_data.append(csv_row)

        time.sleep(1)  # delay to avoid rate limit

    all_playlists.append(playlist_info)

# Save to a JSON file
with open(r'C:\temp\spotifyuser.json', 'w') as f:
    json.dump(all_playlists, f)

# Save to a CSV file
with open(r'C:\temp\spotifyuser.csv', 'w', newline='', encoding='utf-8') as output_file:
    dict_writer = csv.DictWriter(output_file, csv_data[0].keys())
    dict_writer.writeheader()
    dict_writer.writerows(csv_data)
