num = [str(i) for i in range(1, int(input()) + 1)]
n = []
for z in num:
    count = 0
    for i in z:
        count += int(i)
    flag = False
    for j in range(len(n)):
        if n[j][0] == str(count):
            n[j].append(str(count))
            flag = True
            break
    if not flag:
        n.append([str(count)])
print(len(max(n, key=len)))
