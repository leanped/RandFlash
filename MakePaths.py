#!/usr/bin/env python
# coding: utf-8
# %%

import shutil
import os
import random
import ImageDownloader
import Userdata


# %%
def make_addition(main_folder, orig_dict):
    """ Creates a new dataholder dict, which starts as the full list of paths and a subset of paths for the first 
    time it is used.
    """
    assert orig_dict != {} and orig_dict != None
    
    subdirs = os.listdir(main_folder)
    for subdir in subdirs:
        trans = get_trans(subdir)
        eng_word = subdir.split("_")[0]
        if eng_word in orig_dict:
            continue
        if trans == None:
            continue
            
        
        full_path = os.path.join(main_folder, subdir)
        image_path_list = []
        for image_base in os.listdir(full_path):
            image_path_list.append(os.path.join(full_path, image_base))
        
        samp = random.sample(image_path_list, 6)
        
        
        orig_dict[eng_word] = {"all_images": image_path_list,
                       "difficulty" : "Hard",
                       "subset": samp,
                       "translation": trans,
                        "times selected" : 0,
                       "for review" : False}
        
    orig_dict["*metadata"] = {"length": len(data)}
    return data



# %%


def initialize(main_folder, word_dict, storefile):
        
    """ Creates a new dataholder dict, which starts as the full list of paths and a subset of paths for the first 
    time it is used. Checks for any words that dont have enough pictures and deletes those directories. Removes those 
    words form the overall words list as well.
    """
    subdirs = os.listdir(main_folder)
    global data 
    data = {}
    for subdir in subdirs:
        trans = get_trans(subdir)
        eng_word = subdir.split("_")[0]
        if trans == None:
            continue
            
        
        full_path = os.path.join(main_folder, subdir)
        image_path_list = []
        for image_base in os.listdir(full_path):
            image_path_list.append(os.path.join(full_path, image_base))
            
        try:
            assert len(image_path_list) > 10
            samp = random.sample(image_path_list, 6)
            data[eng_word] = {"all_images": image_path_list,
                           "difficulty" : "Hard",
                           "subset": samp,
                           "translation": trans,
                            "times selected" : 0,
                           "for review" : False}
        except (ValueError, AssertionError) as e:
            if eng_word in data:
                del data[eng_word]
            try:
                del word_dict[eng_word]
                shutil.rmtree(os.path.join(main_folder, subdir))
            except:
                print(word_dict, eng_word)
            continue
    Userdata.store_json(word_dict, storefile)
    data["*metadata"] = {"length": len(data)}
    return data
        


# %%


def get_trans(subdir):
    eng_nl = Userdata.english_dutch
    words = subdir.split("_")
    word = words[0]
    return eng_nl.get(word)


# %%


def change_difficulty(word, newVal):
    if newVal not in ["Easy", "Medium", "Hard"]:
        return -1
    data[word]["difficulty"] = newVal 


# %%


def add_new_words(eng_words = None, nl_words = None, dict_alr = False, new_dict = None, orig_dict = None):
    
    good_list = {}
    if (not dict_alr) and (new_dict == None):
        new_dict = dict(zip(eng_words,nl_words))
    
    for key in new_dict:
        if (key not in orig_dict):
            good_list.update({key : new_dict[key]})
            ImageDownloader.make_imgs(key, "images")

    Userdata.english_dutch.update(good_list)
    
    make_addition("images", orig_dict)
    


# %%



#TODO: be able to make a new random sample
def change_samp(word, main_dict):
    image_path_list = main_dict[word]["all_images"]
    samp = random.sample(image_path_list, 6)
    main_dict[word]["subset"] = samp



# %%
def get_plan(working_dict):
    length = len(working_dict)
    ret_val = []
    words = random.sample(list(working_dict.keys()), 10)
    for word in words:
        ret_val.append({"word": word,
                        "subset": data[word]["subset"],
                        "translation": data[word]["translation"]})
    ret_val
    return ret_val

# %%
