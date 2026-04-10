import os

root = "sample_project"

for current_dir, dirs, files in os.walk(root):
    print(f"Current directory: {current_dir}")
    for file_name in files:
        print(f"  - {file_name}")
        
print("   ---   ")

for currenr_dir, dirs, files in os.walk(root):
    for file_name in files:
        if file_name.endswith(".cpp"):
            full_path = os.path.join(current_dir, file_name)
            print(full_path)