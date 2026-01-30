import os

# path=r"C:\Users\prava\OneDrive\Desktop\python\day-4\file_rename.py"

# new_path=r"C:\Users\prava\OneDrive\Desktop\python\day-4\file_renamed.py"

# os.rename(path,new_path)


path=r"C:\Users\prava\OneDrive\Desktop\left-shift\primary-track\pics_backup"

for count,file in enumerate(os.listdir(path),start=1):
    old_path=os.path.join(path,file)
    new_path=os.path.join(path,f"file_{count}.jpg")
    os.rename(old_path,new_path)

print("Files renamed successfully")