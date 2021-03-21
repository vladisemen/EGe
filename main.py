a = open("27-B_2.txt")
n = []
maxx = 0
for line in a:
    n.append(int(line))
lenh = n.pop(0)
for i in range(1,lenh):
    for j in range(i+1,lenh):
        if (n[i]*n[j]) % 14 == 0:
            if n[i]*n[j] > maxx:
                maxx = n[i]*n[j]
print(maxx)
