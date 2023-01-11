B = {2, 4, 6, 8,10,12}
C = {3, 6, 9, 12, 15}

A = set()

for x in range(-1000, 1000):
    if not((not(x in B)) + ((not(x in C)) <= (x in A))):
        A.add(x)

res = 1
for elem in A:
    res *= elem

print(res)

# 640
