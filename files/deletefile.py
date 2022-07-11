import os
import shutil
	
from matplotlib import path

# file = "demo2.txt"
# path = "empty_folder"
path1 = "empty_folder1"

try:	
	os.remove(path1)		#delete a file
	# os.rmdir(path)		#delete an empty directory
	# shutil.rmtree(path1)  #delete a directory containing files

except FileNotFoundError:
	print("that file was not found")
except PermissionError:
	print("you do not have the permission to delete a directory")
except OSError:
	print("you cannot delete * "+path1+" * because it is not empty")
else:
	print(path1+" was deleted")