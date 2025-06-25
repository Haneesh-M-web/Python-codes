print("NAME: Haneesh M")
print("USN:1AY24AI038")
print("SECTION:M")
import os
import re
def fillgap(folder, prefix='spam', extension='.txt'):
    # Regex to match files like spam001.txt
    pattern = re.compile(rf'^{prefix}(\d+){re.escape(extension)}$')
    files = []
    for f in os.listdir(folder):
        match = pattern.match(f)
        if match:
            number = int(match.group(1))
            files.append((number, f))
    if not files:
        print("No matching files found.")
        return
    # Sort files based on number
    files.sort()
    # Get number width (e.g., 3 for spam001)
    number_width = len(re.search(r'\d+', files[0][1]).group())
    expected_num = 1
    for actual_num, filename in files:
        if actual_num != expected_num:
            # Rename file to close the gap
            new_name = f"{prefix}{str(expected_num).zfill(number_width)}{extension}"
            old_path = os.path.join(folder, filename)
            new_path = os.path.join(folder, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed {filename} → {new_name}")
