# spotifyexport
A python project to export Spotify Playlists so that they can be imported to other locations or analyzed further.

This project started as an idea if I wanted to migrate my Spotify Playlists to my own home server or if I wanted to move to another subscription service and compare song offerings.  Additional ideas include analyzing tracks for genre breakdowns, artist prevalence, etc.

------------------------------------------------------------------------------------------------------------------

Requirements:
•	Python
•	Spotify Account
•	Spotify Developer Account (free)

Note, the Spotify Developer Account will provide the API client secret and ID needed for this to analyze your playlists.

------------------------------------------------------------------------------------------------------------------

Two files are included in this repo.
1. playlistexport.py - Queries the Spotify API for your playlist information.  Just update the API portion (lines 8 and 9) with your Spotify Developer information.  Outputs the query as a CSV which can be analyzed further.
2. viewjson.py - For troubleshooting/verification.  Reports the track count for Query.

Example Output:  
playlist_name,	track_name,	artist_name,	album_name,	duration_s,	popularity
FAVrite JAMs,	1.3_5-da3m0nsneverstop.caf,	Mac Quayle,	Mr. Robot, Vol. 1 (Original Television Series Soundtrack),	130.404,	38


------------------------------------------------------------------------------------------------------------------


Feel free to branch off and get this to import into other services.
