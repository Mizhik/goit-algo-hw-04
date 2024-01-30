from pathlib import Path

path = Path("M:/vscPython/repository/goit-algo-hw-04/task2/text.txt")

def get_cats_info(path):
    try:
        with open(path,'r', encoding="utf8") as file:
            file_text = file.readlines()
            outlist = []
            for line in file_text:
                line = line.strip().split(",")
                outlist.append({"id":line[0],"name":line[1],"age":line[2]})
        return outlist
    except FileNotFoundError:
        print(f"{path} - not found")
        return []
cats_info = get_cats_info(path)
print(cats_info)