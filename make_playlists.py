import spotipy
import spotipy.util as util
import sys
import random
import subprocess
import requests
import json

username = "XXXX"
scope = 'user-read-playback-state,playlist-read-private,user-modify-playback-state,playlist-modify-public'
search_str = sys.argv[1]

artist_id_map={}
token = util.prompt_for_user_token(username, scope)

sp = spotipy.Spotify(auth=token)
header = {'Authorization': 'Bearer {}'.format(token)}


res = requests.get("https://api.spotify.com/v1/me/player/devices", headers=header)
devices = res.json()
device_id = devices["devices"][0]['id']

playlist = sp.user_playlist_create(username,"NewPlaylist")
playlist_id = playlist['id']

result = sp.search(q='artist:'+search_str, limit=1)
artist_id = result['tracks']['items'][0]['artists'][0]['id']
print (result['tracks']['items'][0]['id'])
artist_related_artists = sp.artist_related_artists(artist_id)
track_ids = []
for artist_list in artist_related_artists['artists']:
    result = sp.search(q='artist:'+artist_list['name'], limit=50)

    if len(result['tracks']['items']) > 1:
        track_ids.append(random.choice(result['tracks']['items'])['id'])

sp.user_playlist_add_tracks(username, playlist_id, track_ids)

param = {'device_id':device_id,
         'context_uri':'spotify:playlist:%s' % playlist_id}

res = requests.put("https://api.spotify.com/v1/me/player/play", data=json.dumps(param), headers = header)