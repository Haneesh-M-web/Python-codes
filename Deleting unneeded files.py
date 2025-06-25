print("NAME: Haneesh M")
print("USN:1AY24AI038")
print("SECTION:M")
import os
import pathlib
def find(folder, size_limit=100 * 1024 * 1024):
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                file_size = os.path.getsize(file_path)
                if file_size > size_limit:
                    print(f"{file_path} - {file_size / (1024 * 1024):.2f} MB")
            except OSError as e:
                print(f"Error accessing {file_path}: {e}")
find(pathlib.Path.home())
