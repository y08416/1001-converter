from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import signal
import time

print("Hello")
driver = webdriver.Chrome()

try:
    print("Let's try ============")
    driver.get(
    "https://www.1001tracklists.com/tracklist/1b7r32s1/cloonee-ocho-by-gray-area-2022-01-22.html"
    )
    wait = WebDriverWait(driver, 30)
    print("wait ===========")
    element = wait.until(EC.visibility_of_element_located((By.ID, 'middle')))
    
    title = driver.find_element(By.CLASS_NAME, "notranslate")
    
    elem = driver.find_elements(By.CLASS_NAME, "fontL")
    
    elements_list = []
    
    for elem_Loop in elem:
        elements_list.append(elem_Loop.text)
    
    print(title.text)
    print(elements_list)

    time.sleep(30)
    
finally:
    print("finally ============")
    os.kill(driver.service.process.pid,signal.SIGTERM)


