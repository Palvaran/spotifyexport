import pandas as pd
import time
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Setup Spotify API
client_id = 'your-spotify-client-id'
client_secret = 'your-spotify-client-secret'
redirect_uri = 'your-spotify-redirect-uri'
scope = 'playlist-read-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

# Load the CSV file into a pandas DataFrame
df = pd.read_csv(r'C:\temp\spotifyuser.csv')

# Function to fetch genres from artist name
def fetch_genres(artist_name):
    try:
        # Search for the artist
        results = sp.search(q='artist:' + artist_name, type='artist', limit=1)
        artist = results['artists']['items'][0]
        # Return the genres
        return ', '.join(artist['genres'])
    except IndexError:
        # If the artist is not found, return an empty string
        return ''

# Initialize a counter for the progress
counter = 0

# Apply the function to the 'artist_name' column and assign the result to a new 'genres' column
for i, row in df.iterrows():
    artist_name = row['artist_name']
    print(f"Fetching genres for artist: {artist_name}...")
    df.at[i, 'genres'] = fetch_genres(artist_name)
    counter += 1
    print(f"Processed {counter} of {len(df)} artists.")
    # Add a sleep delay to avoid hitting rate limits
    time.sleep(0.1)

# Save the updated DataFrame back to CSV
df.to_csv(r'C:\temp\spotifyuser.csv', index=False)
