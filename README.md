# spotifyexport
A python project to export Spotify Playlists so that they can be imported to other locations or analyzed further.

This project started as an idea if I wanted to migrate my Spotify Playlists to my own home server or if I wanted to move to another subscription service and compare song offerings.  Additional ideas include analyzing tracks for genre breakdowns, artist prevalence, etc.

Requirements:
•	Python
•	Spotify Account
•	Spotify Developer Account (free)

Note, the Spotify Developer Account will provide the API client secret and ID needed for this to analyze your playlists.

Two files are included in this repo.
1. main.py - Queries the Spotify API for your playlist information.  Just update the API portion (lines 8 and 9) with your Spotify Developer information.
2. viewjson.py - For verification.  Reports the track count for Query.

Example Output:  
Playlist Name: Your Top Songs 2022
Number of Tracks: 101
--------------------------------------------------
Playlist Name: Your Top Songs 2021
Number of Tracks: 100
--------------------------------------------------
Playlist Name: Your Top Songs 2020
Number of Tracks: 100
--------------------------------------------------
Playlist Name: Your Top Songs 2019
Number of Tracks: 100
--------------------------------------------------
Playlist Name: Your Top Songs 2018
Number of Tracks: 100
--------------------------------------------------
Playlist Name: Your Top Songs 2017
Number of Tracks: 100
--------------------------------------------------
Playlist Name: Your Top Songs 2016
Number of Tracks: 101

Have fun!
