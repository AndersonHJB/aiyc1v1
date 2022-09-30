from aiyc1v1 import DataRead

# abs_path = r"/Users/huangjiabao/GitHub/aiyc1v1/aiyc1v1/NoteSearch/DataRead.py"
# d = DataRead(path=abs_path)
# d.main()
lst = [1, 2, 3, 4, "\n", "dededed"]

for content in lst:
    if content == "\n":
        print("if")
        # continue
        break
    # content = str(line + 1) + content
    # print(content, end="")
    print(f"{content}Xxxxx")





