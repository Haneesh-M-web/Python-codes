print("NAME:Haneesh M")
print("USN:1AY24AI038")
print("SECTION:M")

import re
import os
def search(folder,element):
    try:
        for file in os.listdir(folder):
            if file.endswith(".txt"):
                file=os.path.join(folder,file)
                try:
                    with open(file,"r") as f:
                      for linenum, line in enumerate(f,1):
                            print(f"File: {file},linne {linenum}: {line.strip()}")
                except Exception as e:
                    print(f"Error reading {file}:{e}")
    except FileNotFoundError:
        print("Folder not found")
    except Exception as e:
        print(f"an unexpected error {e}")
folder=input("Enter any folder name:")
element=input("enter any expression to search:")
search(folder,element)
