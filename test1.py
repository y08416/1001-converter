from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import spotipy.util as util
import os
import signal
import time

print("Hello")

# Spotify認証情報
client_id = "3fe42300fc174ca6bb08c86a53edfbda"
client_secret = "7ef21f4dbabb4fec973f800cf5a666a1"
redirect_uri = "https://example.com"
username = "tim61rw0dk6wbc0l9nmy7lm0q"
scope = 'user-read-playback-state playlist-read-private user-modify-playback-state playlist-modify-public'

# クライアント認証
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# ユーザー認証トークンを取得
try:
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
    print(f"Token acquired: {token}")
except Exception as e:
    print(f"Error acquiring token: {e}")
    raise e

if token:
    sp = spotipy.Spotify(auth=token)

    try:
        print("Let's try ============")
        driver = webdriver.Chrome()
        driver.get("https://www.1001tracklists.com/tracklist/1b7r32s1/cloonee-ocho-by-gray-area-2022-01-22.html")
        wait = WebDriverWait(driver, 30)
        print("wait ===========")
        
        # プレイリスト作成
        try:
            playlist = sp.user_playlist_create(username, "NewPlaylist")
            print(f"Playlist created: {playlist}")
            playlist_id = playlist['id']
        except Exception as e:
            print(f"Error creating playlist: {e}")
            raise e
        
        element = wait.until(EC.visibility_of_element_located((By.ID, 'middle')))
        
        title = driver.find_element(By.CLASS_NAME, "notranslate")
        
        elem = driver.find_elements(By.CLASS_NAME, "fontL")
        
        elements_list = []
        
        # 曲名をスクレイピング
        for elem_Loop in elem: 
            elements_list.append(elem_Loop.text)
        
        # 曲名検索
        test_query = "Chris Lake ft. Alexis Roberts - Turn Off The Lights (Cloonee Remix) BLACK BOOK" 
        result = sp.search(q=test_query, limit=1, offset=0, type='track', market=None) 
            
        print(result)    
            
        time.sleep(30)
        
    finally:
        print("finally ============")
        driver.quit()
else:
    print("Can't get token for", username)
