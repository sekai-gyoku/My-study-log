import os
import sys

if len(sys.argv) < 2:
    print("Usage: python3 project_report.py <target_directory>")
    sys.exit(1)
    
root = sys.argv[1]

cpp_files = []
txt_files = []
log_files = []

for current_dir, dirs, files in os.walk(root):
    for file_name in files:
        full_path = os.path.join(current_dir,file_name)
        
        if file_name.endswith(".cpp"):
            cpp_files.append(full_path)
        elif file_name.endswith(".txt"):
            txt_files.append(full_path)
        elif file_name.endswith(".log"):
            log_files.append(full_path)
            
print("=== Project Report ===")
print("Target directory:",root)
print()

print("[CPP files]")
for path in cpp_files:
    print(path)
print("Total:", len(cpp_files))
print()

print("[TXT files]")
for path in txt_files:
    print(path)
print("Total:", len(txt_files))
print()

print("[CPP files]")
for path in log_files:
    print(path)
print("Total:", len(log_files))
print()