from re import split

with open(r'C:\Downloads\files.txt', 'r', encoding='utf-8') as file:
    result = {}
    for i in file:
        n = split(r'\.|\s', i.strip())
        result.setdefault(n[1], []).append(i.strip())

for i, k in result.items():
    print(sorted(k))
