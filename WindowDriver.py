#!/usr/bin/env python
# coding: utf-8
# %%
import os
import tkinter as tk
from PIL import ImageTk, Image
import MakePaths
import random
import ImageDownloader
from tkinter import ttk
from ttkthemes import ThemedTk
import Userdata


# %%

def setup(loadfile = None, storefile = None):
    """ Takes two optional filename arguments in the form <xxx>.json to load / store as the main dictionary to run this program.
    If no files are provided, a new one will be created."""
    global words
    global canvas
    global images
    global root
    global image_index
    global word_index
    global trans_label
    global trans_text
    global maindata
    curr_wordpairs = Userdata.load_json("word_pairs.json")
    # TODO: Implement loading from save file
    if loadfile != None:
        maindata = Userdata.load_json(loadfile)
        words = MakePaths.get_plan(maindata)
        
    else:
        maindata = MakePaths.initialize("images", curr_wordpairs, "word_pairs.json")
        words = MakePaths.get_plan(maindata)
        if storefile != None:
            Userdata.store_json(maindata, storefile)
        else:
            Userdata.store_json(maindata)
    

def load_images(image_path_files):
    images = []
    for path in image_path_files:
        img = Image.open(path)
        w, h = img.size
        aspect_ratio = w / h
        new_w = min(w, 350)  # ensure images fit within width of canvas
        new_h = int(new_w / aspect_ratio)
        img = img.resize((new_w, new_h), Image.ANTIALIAS)
        images.append(ImageTk.PhotoImage(img, master=None))
    return images

# Create a function to add the images to the canvas with labels
def add_images(images):
    global labels
    labels = []
    for i, image in enumerate(images):
        x = i % 3 * (400 ) + 50
        y = i // 3 * (200 ) + 50
        if y + image.height() > 600:
            break
        labels.append(tk.Label(canvas, image=image))
        labels[-1].image = image
        labels[-1].place(x=x, y=y)
    return labels

        
# Create a function to clear the canvas
def clear_canvas():
    for label in labels:
        label.destroy()
        
def load_next_images():
    # Move on to the next word. This is the only fuction that increments the word.
    global word_index
    global trans_text
    global word_text
    
    word_index += 1
    if word_index >= len(words):
        word_index = 0
    images = load_images(words[word_index]["subset"])
    clear_canvas()
    add_images(images)
    word_text = words[word_index]["word"]
    trans_text = words[word_index]["translation"]
    trans_label.config(text = "")
    english_label.config(text = "")
    
    
def toggle_trans():
    if trans_label.cget("text") == "":
        trans_label.config(text = trans_text )
    else:
        trans_label.config(text = "")
        
def toggle_english():
    if english_label.cget("text") == "":
        english_label.config(text = word_text )
    else:
        english_label.config(text = "")

    
def reroll():
    current_word = words[word_index]["word"]
    MakePaths.change_samp(current_word, maindata)
    new_subset = maindata[current_word]["subset"]
    new_images = load_images(new_subset)
    clear_canvas()
    add_images(new_images)

# TODO: create a button for saving the user data before exiting the program.
# def save_quit():
    
    
    

# %%
def main(words):
    """Take in a subset dictionary of the larger word poulation to run the program on."""
    # Initialize globals
    global canvas
    global images
    global root
    global image_index
    global word_index
    global trans_label
    global trans_text
    global word_text
    global english_label
    word_index = 0
    
    
    trans_text = words[word_index]["translation"]
    word_text = words[word_index]["word"]
    root = ThemedTk(theme = "arc")
    style = ttk.Style()

    # create a custom style for the button with larger font and padding
    style.configure("Custom.TButton", font=("Helvetica", 14), padding=5)
    
    root.title("RandFlash")
    root.geometry("1200x700")

    # Create a Tkinter canvas that can fit the above images

    canvas = tk.Canvas(root, width=1200, height=600)
    canvas.pack()

    english_label = tk.Label(root, text=word_text, font=("Helvetica", 20))
    english_label.place(x = 475, y = 550, anchor = "center")
    toggle_english()

    trans_label = tk.Label(root, text=trans_text, font=("Helvetica", 20))
    trans_label.place(x = 600, y = 550, anchor = "center")
    toggle_trans()
    

    # TODO: create a button for saving the user data before exiting the program.
    
    next_button = ttk.Button(root, text="Volgende", command=load_next_images, style = "Custom.TButton")
    next_button.place(x=1000, y=580, anchor = "center")
                                                  
    trans_button = ttk.Button(root, text="Laat me zien", command=toggle_trans, style = "Custom.TButton")
    trans_button.place(x = 600, y = 595,  anchor = "center")

    reroll_button = ttk.Button(root, text="Randomiseren", command=reroll, style = "Custom.TButton")
    reroll_button.place(x = 150, y = 595,  anchor = "center")
    
    english_button = ttk.Button(root, text="Engels", command=toggle_english, style = "Custom.TButton")
    english_button.place(x = 475, y = 595,  anchor = "center")

                                                  
    # Define the initial folder and image index

    images = load_images(words[word_index]["subset"])

    labels = add_images(images)

    # Start the Tkinter event loop
    root.mainloop()



# %%

# %%
