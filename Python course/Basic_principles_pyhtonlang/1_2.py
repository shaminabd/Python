objects = [1, 2, 1, 2, 3]
ans = 0
tmp = []
for obj in objects: # доступная переменная objects
    if (not(obj in tmp)):
        ans += 1
        tmp.append(obj)

print(ans)