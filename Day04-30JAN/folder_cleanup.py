import os
import shuttle #type: ignore

temp_path=os.environ.get("TEMP")
for file in os.listdir(temp_path):
    try:
        file_path=os.path.join(temp_path,file)
        if os.path.isfile(file_path) or os.path.islink(file_path):
            print(f"deleted {file}.")
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            print(f"deleted {file}.")
            shuttle.rmtree(file_path)
    except Exception as e:
        print(f"Failed to delete {file}.")

print(f"temp folder cleaned.")