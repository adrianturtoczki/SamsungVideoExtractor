import re
import sys
from os import listdir
import tkinter as tk
from tkinter import filedialog, Button

root = tk.Tk()
root.title("Splitter")
def load_file():
    file_name = filedialog.askopenfilename(parent=root,filetypes=[("Images","*.jpg")],title="Choose a file to split")
    if file_name == "":
        exit()
    print(file_name)
    splitter(file_name)
def load_folder():
    directory = filedialog.askdirectory(initialdir='.')
    if directory == "":
        exit()
    print(directory)
    for i in listdir():
        print(i)
        if i.endswith("jpg"):
            splitter(i)
single = Button(text='single', command=load_file,width=30).pack()
batch = Button(text='batch', command=load_folder,width=30).pack()
def splitter(file_name):
    pic_name = file_name+"_pic"+".jpg"
    vid_name = file_name+"_vid"+".mp4"
    try:
        with open(file_name,"r+b") as f:
            data = f.read()
            place = re.search(b"\x4D\x6F\x74\x69\x6F\x6E\x50\x68\x6F\x74\x6F\x5F\x44\x61\x74\x61",data)
            f.seek(place.start()+16)
            vid_data = f.read()
            f.seek(0)
            pic_data = f.read(place.start())
        #save_to = filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("jpg","*.jpg"),("mp4","*.mp4"),("all files","*.*")))
        with open(vid_name,"w+b") as f:
            f.write(vid_data)
        with open(pic_name,"w+b") as f:
            f.write(pic_data)  
        print("Splitting succesful.")
    except:
        print("Splitting not succesful. on file %s."%file_name)
root.mainloop()
