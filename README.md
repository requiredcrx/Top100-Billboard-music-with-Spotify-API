# Awesome Spotify Playlist Creator 🎶

## Overview

The Awesome Spotify Playlist Creator is a fun and interactive Python project that allows you to create awesome Spotify playlists based on Billboard's top 100 songs from a specific year. The project uses Beautiful Soup for web scraping, Spotipy for Spotify API integration, and python-dotenv for managing environment variables. With just a few simple steps, you can create a personalized playlist and rock to your favorite hits!

## Prerequisites

Before you get started, make sure you have the following:

- Python 3.x installed on your system
- A Spotify Developer Account (to get your `client_id`, `client_secret`, and `redirect_uri`)
- Billboard's top 100 chart data for your desired year (we'll do the web scraping magic!)

## Getting Started

1. Clone the project repository from GitHub to your local machine.

2. Install the required Python packages by running the following command in your terminal:

   ```bash
   pip install beautifulsoup4 requests spotipy python-dotenv
- 1. Create a Spotify Developer Account and register your application to get your client_id, client_secret, and redirect_uri. These credentials will be used to authenticate with Spotify's API.
- 2. Create a file named ```.env``` in the project's root directory and add your Spotify credentials as environment variables. For example:
     
     ```SPOTIPY_CLIENT_ID=your_client_id_here```
     ```SPOTIPY_CLIENT_SECRET=your_client_secret_here```
     ```SPOTIPY_REDIRECT_URI=your_redirect_uri_here```
## How to Use
1. Run the script by executing the following command:
```
python create_spotify_playlist.py
```
2. Enter the year for which you want to create the playlist. The script will automatically scrape Billboard's top 100 chart for that year.
3. The script will create a text file named top100.txt containing the names of the top 100 songs for the chosen year.
4. The Awesome Spotify Playlist Creator will then authenticate with Spotify using your credentials and create a new private playlist named after the chosen year.
5. Sit back and relax while the script adds your favorite Billboard hits to the new playlist!

## Additional Features

- The project allows you to set a custom playlist name and description, making your playlist truly unique.
- Exception handling ensures that the script skips any songs that cannot be found on Spotify, so you won't miss out on any of your favorites.

## Show Off Your Playlist!
Once your Awesome Spotify Playlist is created, share it with friends, family, or the world! Enjoy your handpicked collection of top hits from Billboard's chart and bring back the memories from your favorite year.


Happy playlist creating! 🎉🎵

