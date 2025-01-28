import os
import shutil 

from_dir = "C:/Users/Manya Manikandan/Downloads/C102_assets-main"

to_dir = "C:/Users/Manya Manikandan/Downloads/102"

files = os.listdir(from_dir)
#print(files)

for file_name in files :
    name,extension = os.path.splitext(file_name)
    #print(name,extension)
    if extension == '':
        continue
    if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path_1 = from_dir + '/' + file_name
        path_2 = to_dir + '/' + "images"
        path_3 = to_dir + '/' + "images" + '/' + file_name
        
        #print(f"path 1: {path_1}" )
        #print(f"path 3: {path_3}" )
        
        if os.path.exists(path_2):
          print("Moving " + file_name + ".....")

          # Move from path1 ---> path3
          shutil.move(path_1, path_3)

        else:
          os.makedirs(path_2)
          print("Moving " + file_name + ".....")
          shutil.move(path_1, path_3)
