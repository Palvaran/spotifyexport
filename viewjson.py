import json

with open('C:\\temp\\spotifyuser.json', 'r') as f:
    data = json.load(f)

for playlist in data:
    print(f"Playlist Name: {playlist['name']}")
    print(f"Number of Tracks: {len(playlist['tracks'])}")
    print("-" * 50)  # separator
