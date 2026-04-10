import os
import sys

if len(sys.argv) < 3:
    print("Usage: python3 project_report_save.py <target_directory> <output_file>")
    sys.exit(1)

root = sys.argv[1]
output_file = sys.argv[2]

cpp_files = []
txt_files = []
log_files = []

for current_dir, dirs, files in os.walk(root):
    for file_name in files:
        full_path = os.path.join(current_dir, file_name)

        if file_name.endswith(".cpp"):
            cpp_files.append(full_path)
        elif file_name.endswith(".txt"):
            txt_files.append(full_path)
        elif file_name.endswith(".log"):
            log_files.append(full_path)

with open(output_file,"w",encoding="utf-8") as f:
    f.write("=== Project Report ===\n")
    f.write(f"Target directory: {root}\n\n")
    
    f.write("[CPP files]\n")
    for path in cpp_files:
        f.write(path + "\n")
    f.write(f"Total: {len(cpp_files)}\n\n")
    
    f.write("[TXT files]\n")
    for path in txt_files:
        f.write(path + "\n")
    f.write(f"Total: {len(txt_files)}\n\n")
    
    f.write("[LOG files]\n")
    for path in log_files:
        f.write(path + "\n")
    f.write(f"Total: {len(log_files)}\n\n")
    
print(f"Report saed to {output_file}")