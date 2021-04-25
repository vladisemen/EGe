file = open('text.txt')
n = int(file.readline())
dlina = 1
Max_dlina = 1
a = []
b = []
dlina1 = 1
for line in file:
    a1, b1 = line.split()
    a.append(a1)
    b.append(b1)
for i in range(n - 1):
    if b[i] == a[i + 1]:
        dlina += 1
    elif b[i] == b[i + 1]:

        for j in range(i+1, n-1):
            if b[j] == a[j + 1]:
                dlina1 += 1
            elif b[j] == b[j + 1]:
                a[j + 1], b[j + 1] = b[j + 1], a[j + 1]
                dlina1 += 1
            else:
                if dlina1 > Max_dlina:
                    Max_dlina = dlina1
                dlina1 = 1
                break

        a[i+1],b[i+1] = b[i+1],a[i+1]
        dlina += 1
    else:
        if dlina > Max_dlina:
            Max_dlina = dlina
        dlina = 1
print(Max_dlina)







