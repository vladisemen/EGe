n = open("27-A.txt")
s1 = 0
s2 = 0
s3 = 0
mr =100000
for i in n:
    a,b,c = map(int,i.split())
    if a >= b and a >=c :
        s1 += a
        if b >= c:
            s2 += b
            s3 += c
        else:
            s2 += c
            s3 += b
    elif b >= a and b >= c:
        s1 += b
        if a >= c:
            s2 += a
            s3 += c
        else:
            s2 += c
            s3 += a
    else:
        s1 += c
        if a >= b:
            s2 += a
            s3 += b
        else:
            s3 += b
            s2 += a
    if abs(a-b) %2 != 0 and abs(a-b) < mr:
        mr = abs(a-b)
    elif abs(a-c) %2 != 0 and abs(a-c) < mr:
        mr = abs(a-c)
if (s2 + s3) % 2 != 0:
    print(s1)
else:
    print(s1-mr)
