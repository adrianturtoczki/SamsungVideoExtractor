import re
import sys
import os

file_name = sys.argv[1]
    
pic_name = file_name+"_pic"+".jpg"
vid_name = file_name+"_vid"+".mp4"

if len(sys.argv) > 1:
    with open(file_name,"r+b") as f:
        data = f.read()
        place = re.search(b"\x4D\x6F\x74\x69\x6F\x6E\x50\x68\x6F\x74\x6F\x5F\x44\x61\x74\x61",data)
        f.seek(place.start()+16)
        data = f.read()
    with open(vid_name,"w+b") as f:
        f.write(data)
    print("Splitting succesful.")
