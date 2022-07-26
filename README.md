# Text to Spotify Playlist
Transforms .txt files into a spotify playlist


## Usage
Make sure to install all the requirements by using
```
pip install -r requirements.txt
```

Change `playlist_id` _Line 5_ to your playlist's uid
<br>
Here is how you can get that
<br>
![How to get playlist uri](playlist_uri.gif)

Add the songs you want to `music.txt`
<br>
Now you're good to go, Run
```
py main.py
```
#### Warning: If your music list is too big it may crash so just rerun it


## How it works
`main.py` reads every line from `music.txt` and searches for it in spotify database, It then adds the first (most popular) result to the playlist.