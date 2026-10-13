from textnode import TextNode, TextType
import os
import shutil

def source_to_destination(srcpath, destpath):
    if os.path.exists(destpath):
        shutil.rmtree(destpath)
    os.mkdir(destpath)
    files = os.listdir(srcpath)
    for file in files:
        if os.path.isfile(os.path.join(srcpath, file)):
            shutil.copy(os.path.join(srcpath, file), destpath)
        else:
            source_to_destination(os.path.join(srcpath, file), os.path.join(destpath, file))
            


def main():
    
    source_to_destination("static", "public")    

main()