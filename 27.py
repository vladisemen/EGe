n = open("27-B_demo.txt")
s = 0
minr = 10000
for line in n:
    a,b = map(int,line.split())
    s +=max(a,b)
    if abs(a-b) < minr and abs(a-b) % 3!= 0:
        minr = abs(a-b)
if s % 3 != 0:
    print(s)
else:
    print(s-minr)






