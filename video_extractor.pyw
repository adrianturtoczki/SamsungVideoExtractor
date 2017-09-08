import re
import sys
import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_name = filedialog.askopenfilename(parent=root,title="Choose a file to split")
if file_name == "":
    exit()
#file_name = sys.argv[1]
pic_name = file_name+"_pic"+".jpg"
vid_name = file_name+"_vid"+".mp4"

if 2 > 1:
    with open(file_name,"r+b") as f:
        data = f.read()
        place = re.search(b"\x4D\x6F\x74\x69\x6F\x6E\x50\x68\x6F\x74\x6F\x5F\x44\x61\x74\x61",data)
        f.seek(place.start()+16)
        vid_data = f.read()
    with open(vid_name,"w+b") as f:
        f.write(vid_data)
#    with open(pic_name,"w+b") as f:
#        f.write(pic_data)  
    print("Splitting succesful.")
