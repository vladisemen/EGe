file = open("text.txt")
f = file.readline()
M = 1
m = 1
for i in range(len(f)):
    if f[i] == ")" and f[i + 1] == ")":
        m += 1
    else:
        if m > M:
            M = m
        m = 1
print(M)