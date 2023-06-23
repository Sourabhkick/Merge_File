
with open(r"C:\Users\Lazard\Desktop\split\txt2.txt") as td:
    data = td.read()
with open(r"C:\Users\Lazard\Desktop\split\txt1.txt") as td:
    data2 = td.read()
data += "\n"
data += data2
with open('merge.txt', 'w') as td:
    td.write(data)


















