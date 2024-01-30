from pathlib import Path

path = Path("M:/vscPython/repository/goit-algo-hw-04/task1/text.txt")

def total_salary(path):
    try:
        with open(path, 'r', encoding="utf8") as file:
            file = file.readlines()
            outlist = []
        for line in file:
            line = line.split(',')
            outlist.append(int(line[1]))    
        all_s = sum(outlist)
        average_sum = int(all_s/len(outlist))
        result = (all_s,average_sum)
        return result
    except FileNotFoundError:
        print(f"{path} - not found")
        return () 

total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")