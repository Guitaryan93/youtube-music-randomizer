# YouTube Music Randomizer. Get new artists you never heard of! Like shopping
# in HMV or on iTunes back in the olden' times...

from ytmusicapi import YTMusic
from random import randint
import json

# YouTube API object
ytmusic = YTMusic()

# Import the english word file and pull a random word
with open("words_dictionary.json", "r") as file:
    eng_dict = json.load(file)

all_words = list(eng_dict.keys())

full_search_string = all_words[randint(0, len(all_words) - 1)]

# Limit search word to 5 characters for less chance of nothing being returned
search_string = full_search_string[0:5]

# Call API to get search results for artists and songs
artist_search_results = ytmusic.search(search_string, "artists", limit=200)
song_search_results = ytmusic.search(search_string, "songs", limit=200)

# Build a list of lists for the results from the returned API data
# Create a list for each result that contains the artist name and song title
# and the browseID that is used with the YouTube music URL to access the 
# artists page
results_list = []
for artist in artist_search_results:
    results_list.append([artist["artist"], artist["browseId"]])

for song in song_search_results:
    results_list.append([song["artists"][0]["name"] + " - " + song["title"],
                        song["artists"][0]["id"]])

# Show the random result and the URL to see the artists site page
if len(results_list) == 0:
    print("\nNo results found...")
else:
    random_result = results_list[randint(0,len(results_list) - 1)]
    print(f"\n{random_result[0]}\n")
    print(f"https://music.youtube.com/channel/{random_result[1]}\n")

