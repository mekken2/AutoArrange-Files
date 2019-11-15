'''
Solely developed by PRIYANSHU KUMAR 
An almost basic Python script to Arrange files based on extensions
Permitted for own usage(Under MIT License)
'''
# TODO:Save the moved file data into a database and ignore those files (or check only current dir.)
# TODO:Make only those folders which are needed as per the Extension requirement
# TODO:Make it to ignore itself and not get moved somewhere else
# TODO:Convert the .py file to .exe to run anywhere just by double click

# Importing needed modules
import time
import os
import sys
import shutil

# Saving the path of Current Working Directory
rootdir = os.getcwd()

# Function to Create different directories to store specific files


def create_the_directories():

    i = 0
    j = 0
    k = 0
    l = 0
    m = 0
    n = 0

    for root, dirs, files in os.walk(rootdir):
        for dir in dirs:
            print(dir)

            if dir.lower() == "music" or dir.lower() == "musics":
                i += 1
            if dir.lower() == "video" or dir.lower() == "videos":
                j += 1
            if dir.lower() == "book" or dir.lower() == "books":
                k += 1
            if dir.lower() == "other" or dir.lower() == "others":
                l += 1
            if dir.lower() == "program" or dir.lower() == "programs":
                m += 1
            if dir.lower() == "image" or dir.lower() == "images":
                n += 1

    # Create the directory if it is not already present
    if i == 0:
        os.mkdir(rootdir + "\\Music")
    if j == 0:
        os.mkdir(rootdir + "\\Video")
    if k == 0:
        os.mkdir(rootdir + "\\Books")
    if l == 0:
        os.mkdir(rootdir + "\\Others")
    if m == 0:
        os.mkdir(rootdir + "\\Programs")
    if n == 0:
        os.mkdir(rootdir + "\\Images")


# Calling the Function to start creating directories
create_the_directories()

# Function to move the file from source to destination


def move_the_file(source, destination):
    #os.rename(source, destination)
    shutil.move(source, destination)
    #os.replace(source, destination)

# Function to Check the extension of file and move it to its specific directory


def checking_files():
    for root, dirs, files in os.walk(rootdir):
        ind = 0
        # Checking the extensions
        for file in files:
            ind += 1
            if "mp4" in file or "MP4" in file \
                    or "wmv" in file or "WMV" in file \
                    or "avi" in file or "AVI" in file:
                source = root + "\\" + file
                print(source)
                destination = rootdir+"\\Video\\" + file
                print(destination)
                move_the_file(source, destination)
            elif "jpg" in file or "JPG" in file \
                    or "jpeg" in file or "JPEG" in file \
                    or "png" in file or "PNG" in file \
                    or "bmp" in file or "BMP" in file:
                source = root + "\\" + file
                print(source)
                destination = rootdir+"\\Images\\" + file
                print(destination)
                move_the_file(source, destination)
            elif "mp3" in file or "MP3" in file \
                    or "wav" in file or "WAV" in file \
                    or "aif" in file or "AIF" in file:
                source = root + "\\" + file
                print(source)
                destination = rootdir+"\\Music\\" + file
                print(destination)
                move_the_file(source, destination)
            elif "pdf" in file or "PDF" in file \
                    or "doc" in file or "DOC" in file \
                    or "txt" in file or "TXT" in file:
                source = root + "\\" + file
                print(source)
                destination = rootdir+"\\Books\\" + file
                print(destination)
                move_the_file(source, destination)
            elif "exe" in file or "EXE" in file \
                    or "app" in file or "APP" in file \
                    or "vb" in file or "VB" in file:
                source = root + "\\" + file
                print(source)
                destination = rootdir+"\\Programs\\" + file
                print(destination)
                move_the_file(source, destination)
            # else:
            #     source = root + "\\" + file
            #     print(source)
            #     destination = rootdir+"\\Others\\" + file
            #     print(destination)
            #     move_the_file(source, destination)


# Calling the function to check and move the files
while True:
    checking_files()
    time.sleep(1)
