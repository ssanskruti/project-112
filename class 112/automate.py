import os
import shutil

source="C:/Users/91976/Downloads"
destination="C:/Users/91976/Downloads"
files=os.listdir(source)

for file in files:
    name,ext=os.path.splitext(file)
    if ext=="":
        continue
    if ext in [".gif",".png",".jpg",".jpeg",".jfif"]:
        path1=source+"/"+file
        path2=destination+"/"+"images"
        path3=destination+"/"+"images"+"/"+file
        
        if os.path.exists(path2):
            print("Moving")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving")
            shutil.move(path1,path3)
