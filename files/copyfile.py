# copyfile() = copies content of a file
# copy() = copyfile() + permission mode + destination can be a directory
#copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile("demo.txt","/Users/sumanth/Desktop/text.txt") #source,destination
shutil.copyfile("demo.txt"" text.txt") #source,destination
