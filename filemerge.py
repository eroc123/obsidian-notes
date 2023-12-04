import os

print(os.getcwd())
target = open("D:\\Library Folders\\OneDrive\\Pictures\\Documents\\Obsidian Vault\\Geography A level\\Export\\urban regeneration.md", "w+")

f=[]
filePath = "D:\\Library Folders\\OneDrive\\Pictures\\Documents\\Obsidian Vault\\Geography A level\\Urban\\L7 - Regeneration"

Walk = os.walk(filePath,topdown=True)
layer = 2
for (dirpath, dirnames, filenames) in Walk:
    if dirpath.find("Images") == -1: #takes all the files that are not in the images folder
        f.extend(filenames)
for i in f:
    target.write('\n')
    target.write("### {} ".format(i[:-3]) + '\n')
    target.write("![[{}]]".format(i))
  
target.close()