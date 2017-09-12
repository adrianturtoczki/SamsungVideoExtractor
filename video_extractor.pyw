import re
import sys
from os import listdir
from tkinter import Tk, filedialog, Button, IntVar, Checkbutton
from tkinter.ttk import Progressbar

root = Tk()
root.title("Extractor")
def load_file():
    file_name = filedialog.askopenfilename(parent=root,filetypes=[("Images","*.jpg")],title="Choose a file to split")
    if file_name == "":
        exit()
    print(file_name)
    extractor(file_name,vid_in,img_in)
def load_folder():
    directory = filedialog.askdirectory(initialdir='.')
    if directory == "":
        exit()
    print(directory)
    for i in listdir():
        print(i)
        if i.endswith("jpg"):
            extractor(i,vid_in,img_in)

single = Button(text='single', command=load_file,width=30).pack()
batch = Button(text='folder', command=load_folder,width=30).pack()
vid_in = IntVar()
vid_in.set(1)
img_in = IntVar()
img_in.set(1)
ch = Checkbutton(root, text='video', variable=vid_in).pack()
ch = Checkbutton(root, text='image', variable=img_in).pack()
def extractor(file_name,vid_in,img_in):
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
        if vid_in.get() == 1:
            with open(vid_name,"w+b") as f:
                f.write(vid_data)
        if img_in.get() == 1:
            with open(pic_name,"w+b") as f:
                f.write(pic_data)  
        print("Extracting succesful.")
    except:
        print("Extracting not succesful. On file %s."%file_name)
root.mainloop()
