a, b = map(str,input().split())
if len(a) > len(b):
    b = '0' * (len(a) - len(b)) + b
else:
    a = '0' * (len(b) - len(a)) + a
res = int()
k = 0
l = 0
previous_remainder = -8
for i in a[::-1]:
    k += 1
    for j in b[::-1]:
        l += 1
        if k == l:
            summ = (int(i) + int(j)) % 10
            current_res = summ * (10 ** (k -1))
            if previous_remainder > 0:
                current_res += previous_remainder * (10 ** (k -1))
            res += current_res
            previous_remainder = (int(i) + int(j)) // 10
    l = 0
res += previous_remainder * (10 ** k)
print(res)
