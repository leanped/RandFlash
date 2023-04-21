#!/usr/bin/env python
# coding: utf-8
# %%

import os
import json 
import requests
import selenium
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import base64
import time
import urllib.request
import random


# %%



def make_imgs(query, mother_folder = "images"):
    """given a query and target parent folder,  create a subfolder containing images of that query"""
    DRIVER_PATH = '/usr/local/bin/chromedriver'

    SAVE_FOLDER = os.path.join(mother_folder, query+'_images/')

    GOOGLE_IMAGES = 'https://www.google.com/search?q='+ query + '&rlz=1C5CHFA_enGB937GB937&sxsrf=ALeKk02twWeFWJCESdRh27hZxC0iZwBS6w:1617724623722&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiu0ans_envAhUkT98KHZ7CDiMQ_AUoAXoECAEQAw&biw=714&bih=732'
    if not os.path.exists(SAVE_FOLDER):
        os.makedirs(SAVE_FOLDER)

    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get(GOOGLE_IMAGES)
    driver.find_elements

    # Scroll to the end of the page
   
    counter = 0
    total_elems = []
    for i in range(6):     
        scroll_to_end(driver)
        image_elements = driver.find_elements(By.CLASS_NAME, "rg_i")
        total_elems.extend(image_elements)
        
    
    total_elems = list(set(total_elems))
    for idx in range(len(total_elems)):
        if (counter >50):
            break
        image = total_elems[idx]
        if (image.get_attribute('src') is not None):
            my_image = image.get_attribute('src').split('data:image/jpeg;base64,')
            filename = SAVE_FOLDER+ query+str(counter)+'.jpeg'
            if(len(my_image) >1): 
                with open(filename, 'wb') as f: 
                    f.write(base64.b64decode(my_image[1]))
                    counter += 1
                    
#             else: 
                
#                 urllib.request.urlretrieve(image.get_attribute('src'), SAVE_FOLDER + query+ str(counter)+'.jpeg')
            
    driver.quit()


# %%


def scroll_to_end(driver):
       driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
       time.sleep(10)


# %%
def make_img_folder(dict_words, folder = "images"):
    
    """ makes all the images given a dictionary like {"english word": "nederlands woord"} and will not make duplicate folders.
    """
    created_already = os.listdir(folder)
    created_already = [(subfolder.split("_"))[0] for subfolder in created_already]
    count = 0
    for key in dict_words:
        if key not in created_already:
            count += 1
    
    for key in dict_words: 
        if key not in created_already:
            print(str(count) + " searches remaining")
            make_imgs(key, folder)
            count -= 1

# %%
