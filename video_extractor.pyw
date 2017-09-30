import re
import sys
from os import listdir
import os.path
from tkinter import Tk, Button, IntVar, Checkbutton, filedialog
from tkinter.ttk import Progressbar

root = Tk()
root.title("Extractor")

def save_to_folder():
    save_to = filedialog.askdirectory(initialdir='.')
    if save_to == "":
        exit()
    return save_to
def load_file():
    file_name = filedialog.askopenfilename(parent=root,filetypes=[("Images","*.jpg")],title="Choose a file to split")
    if file_name == "":
        exit()
    save_to = save_to_folder()
    extractor(file_name,vid_in,img_in,save_to)
def load_folder():
    directory = filedialog.askdirectory(initialdir='.')
    if directory == "":
        exit()
    save_to = save_to_folder()
    for i in listdir():
        print(i)
        if i.endswith("jpg"):
            extractor(i,vid_in,img_in,save_to)

single = Button(text='single', command=load_file,width=30).pack()
batch = Button(text='folder', command=load_folder,width=30).pack()
vid_in = IntVar()
vid_in.set(1)
img_in = IntVar()
img_in.set(0)
ch = Checkbutton(root, text='video', variable=vid_in).pack()
ch = Checkbutton(root, text='image', variable=img_in).pack()
def extractor(file_name,vid_in,img_in,save_to):
    file_name = os.path.basename(file_name)
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
        save_folder = save_to+"/VideoExtractor"
        if not os.path.exists(save_folder): #Create folder
            os.makedirs("VideoExtractor")
        if vid_in.get() == 1:
            with open(os.path.join(save_folder, vid_name),"w+b") as f:
                f.write(vid_data)
        if img_in.get() == 1:
            with open(os.path.join(save_folder, pic_name),"w+b") as f:
                f.write(pic_data)
        print("Extracting succesful in %s."%save_folder)
    except Exception as e:
        print("Extracting not succesful. On file %s. Error: %s"%(file_name,e))
    try:
        os.system('exiftool "-FileCreateDate<CreateDate" '+save_folder)
    except e as Exception:
        print(Exception)
        
root.mainloop()
