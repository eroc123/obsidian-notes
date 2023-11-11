import os

print(os.getcwd())
target = open(".\\Export\\coastsL2.md", "w+")

f=[]
filePath = ".\\Geography A level\\Coasts\\L2 - Coastal processes and landforms"

Walk = os.walk(filePath,topdown=True)
layer = 2
for (dirpath, dirnames, filenames) in Walk:
    if dirpath.find("Images") == -1: #takes all the files that are not in the images folder
        f.extend(filenames)
for i in f:
    target.write("![[{}]]".format(i))
  
target.close()