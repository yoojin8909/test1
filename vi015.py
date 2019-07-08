f = open("vi014.py",'r')
r=f.readlines()
f.close()

for s in r:
    print(s.strip())
