import os

root = "sample_project"

cpp_count=0
txt_count=0
log_count=0

for current_dir, dirs, files in os.walk(root):
    for file_name in files:
        if file_name.endswith(".cpp"):
            cpp_count+=1
        elif file_name.endswith(".txt"):
            txt_count+=1
        elif file_name.endswith(".log"):
            log_count+=1
            
print("Summary:")
print("cpp files:",cpp_count)
print("txt files:",txt_count)
print("log files:",log_count)