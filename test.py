from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from spotipy.oauth2 import SpotifyClientCredentials

import spotipy
import os
import signal
import time
import pprint
import spotipy.util as util

print("Hello")
driver = webdriver.Chrome()

#Spotifyインスタンスの作成

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id="3fe42300fc174ca6bb08c86a53edfbda", #Client ID
	client_secret="7ef21f4dbabb4fec973f800cf5a666a1", #Client Secret
    redirect_uri="https://example.com",               #Redirect Url
    scope= 'user-read-playback-state,playlist-read-private,user-modify-playback-state,playlist-modify-public' #scope
    )
)

try:
    print("Let's try ============")
    driver.get(
    "https://www.1001tracklists.com/tracklist/1b7r32s1/cloonee-ocho-by-gray-area-2022-01-22.html"
    )
    wait = WebDriverWait(driver, 30)
    print("wait ===========")
    
    #プレイリスト作成
    username = "tim61rw0dk6wbc0l9nmy7lm0q"
    # scope = 'user-read-playback-state,playlist-read-private,user-modify-playback-state,playlist-modify-public'
    # token = util.prompt_for_user_token(username, scope)
    # sp = spotipy.Spotify(auth=token)
    # header = {'Authorization': 'Bearer {}'.format(token)}

    playlist = sp.user_playlist_create(username,"NewPlaylist")
    playlist_id = playlist['id']

    
    
    element = wait.until(EC.visibility_of_element_located((By.ID, 'middle')))
    
    title = driver.find_element(By.CLASS_NAME, "notranslate")
    
    elem = driver.find_elements(By.CLASS_NAME, "fontL")
    
    elements_list = []
    
    #曲名をスクレイピング
    for elem_Loop in elem: 
        elements_list.append(elem_Loop.text)
    
    #曲名検索
    test_query = "Chris Lake ft. Alexis Roberts - Turn Off The Lights (Cloonee Remix) BLACK BOOK" 
    result = sp.search(q=test_query , limit=1, offset=0, type='album', market=None) 
        
    print(result)    
        
    time.sleep(30)
    
finally:
    print("finally ============")
    os.kill(driver.service.process.pid,signal.SIGTERM)


