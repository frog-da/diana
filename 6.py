result_search = []
x_y = []
for x in '0123456789ABC':
    for y in '0123456789ABC':
        t = int(x + '23' + x + '5', 22) - int('67' + y + '9' + y, 13)
        if t % 57 == 0:
            if x != '0':
                result_search.append(t)
                x_y.append(x+y)
if result_search:
    print(result_search[x_y.index(min(x_y))] // 57)
# output: 25871
