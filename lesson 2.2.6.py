spis = [input().split(', ') for _ in range(int(input()))]
n = []
for i in min(spis, key=len):
    count = len(spis)
    for j in range(len(spis)):
        if i in spis[j]:
            count -= 1
    if count == 0:
        n.append(i)
if not n:
    print('Сериал снять не удастся')
else:
    print(*sorted(n), sep=', ')
