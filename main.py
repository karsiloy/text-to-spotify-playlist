import spotipy
from spotipy.oauth2 import SpotifyOAuth


playlist_id = "2XTmm0G1RwVYQdWrLf0gJf"

scope = "playlist-read-collaborative " \
        "playlist-modify-public " \
        "playlist-read-private " \
        "playlist-modify-private "

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="3602ad5e5755443b882779e6dba5b285",
                                               client_secret="a657fbe4bc3342518a41fe2530b30416",
                                               redirect_uri="http://localhost:8080/callback/",
                                               scope=scope))

li = list()
playlist_data = sp.playlist(playlist_id)
amount = 100

if playlist_data["tracks"]["total"] < 100:
    amount = int (playlist_data["tracks"]["total"])

with open("./music.txt", encoding="utf8") as f:
    for i in f.readlines():
        i = i.strip()
        found = False
        song = sp.search(i)
        try:
            song_id = song["tracks"]["items"][0]["uri"]
        except IndexError:  # Nothing Found on Spotify
            print(f"{i} is not found on spotify")
            continue

        if len(li) == 99:  # We can only send 100 tracks
            sp.playlist_add_items(playlist_id, li)
            print("TAKING A BREAK")
            li.clear()
            li.append(song_id)
            continue
        else:
            for j in range(amount):
                if song_id == playlist_data["tracks"]["items"][j]["track"]["uri"]:
                    print(f'{playlist_data["tracks"]["items"][j]["track"]["name"]} is already in the playlist')
                    found = True

        if found:  # This is already in the playlist
            continue
		
        if song_id in li:  # This is already being added
            continue
		
        print(f'Adding "{song["tracks"]["items"][0]["name"]}" to the playlist')
        li.append(song_id)

    sp.playlist_add_items(playlist_id, li)
