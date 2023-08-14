import tkinter
from tkinter import filedialog
import os

def Browsefolder(file):
    root = tkinter.Tk()
    root.withdraw()
    if file:
        filename = filedialog.askopenfilename(
        filetypes=(
            ("MP4 files", "*.mp4"),
            ("Python Files", ("*.py", "*.pyx")),
            ("All Files", "*.*")
        ))
        return filename
    
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print ("You chose: %s" % tempdir)
    file_path_variable = tempdir
    print ("\nfile_path_variable = ", file_path_variable)
    return str(file_path_variable)