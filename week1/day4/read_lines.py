with open("sample_project/docs/notes.txt","r",encoding="utf-8") as f:
    lines = f.readlines()
    
print("Line count:",len(lines))
for i,line in enumerate(lines,start=1):
    print(f"{i}: {line.strip()}")