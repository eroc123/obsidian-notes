import os

print(os.getcwd())
target = open(".\\Export\\urbanL2.md", "w+")

f=[]
filePath = ".\\Geography A level\\urban\\L2 - Transport Issues"

Walk = os.walk(filePath,topdown=True)
layer = 2
for (dirpath, dirnames, filenames) in Walk:
    if dirpath.find("Images") == -1: #takes all the files that are not in the images folder
        f.extend(filenames)
for i in f:
    target.write("![[{}]]".format(i))
  
target.close()