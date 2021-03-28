s = 0
def F(n):
    if n <= 5:
        return n + 15
    if n > 5 and n % 2 == 0:
        return F(n//2) + n*n*n - 1
    if n > 5 and n % 2 != 0:
        return F(n-1) + 2*n*n + 1
for i in range(1,1001):
     m = str(F(i))
     if m.count("8") >= 2:
         s +=1
print(s)







