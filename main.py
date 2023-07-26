import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

load_dotenv()
# Declaring needed Variables
year = input("What year would you like to travel to in YY-MM-DD? ")
URL = f"https://www.billboard.com/charts/hot-100/{year}"
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
Spotifyusername = os.getenv("SPOTIPY_USERNAME")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

Redirect_URL = "https://example.com/"
scope = "playlist-read-private, " \
        "user-read-currently-playing, " \
        "user-read-currently-playing, " \
        "user-follow-read, playlist-modify-private"


# SCRAPING BILLBOARD TOP 100 CHARTS WITH BEAUTIFUL SOUP
response = requests.get(URL)
billboard_website = response.text
soup = BeautifulSoup(billboard_website, "html.parser")
top100 = soup.find_all("h3", class_="u-max-width-330")

# Authenticating Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=Redirect_URL,
    scope=scope)
)

song_uris = []
for song in top100:
    song_name = song.getText().strip()
    result = sp.search(q=song_name, type="track")

    if result["tracks"]["items"]:
        song_uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(song_uri)
    else:
        print(f"Song {song_name} not found on Spotify")

# Creating a new playlist on Spotify
playlist_name = f"Billboard Hot 100 - {year}"
description = "Top 100 songs on Billboard charts for the specified year."

playlist = sp.user_playlist_create(user=Spotifyusername,
                                   name=playlist_name,
                                   description=description,
                                   public=False)
# Adding songs to playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)


