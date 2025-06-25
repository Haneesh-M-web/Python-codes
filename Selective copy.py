print("NAME: Haneesh M")
print("USN:1AY24AI038")
print("SECTION:M")
import os
import shutil
def selective(source, extensions, destination):
    source = os.path.abspath(source)
    destination = os.path.abspath(destination)
    print(f"Looking in '{source}' for files with extensions: {', '.join(extensions)}")
    for foldername, subfolders, filenames in os.walk(source):
        for filename in filenames:
            _, ext = os.path.splitext(filename)
            if ext.lower() in extensions:
                source_file = os.path.join(foldername, filename)
                print(f"Copying '{source_file}' to '{destination}'")
                shutil.copy(source_file, destination)
extensions = ['.php', '.py']
source = 'randomFolder'
destination = 'selectiveFolder'
selective(source, extensions, destination)
