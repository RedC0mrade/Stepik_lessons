glas = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
word = input()
words = [input() for i in range(int(input()))]
n = []

for i in word:
    if i in glas:
        word = word.replace(i, '*', 1)
    else:
        word = word.replace(i, '_', 1)
word = word.rstrip('_')
for j in words:
    n1 = j
    for i in j:
        if i in glas:
            j = j.replace(i, '*', 1)
        else:
            j = j.replace(i, '_', 1)
    j = j.rstrip('_')
    if word == j:
        n.append(n1)
print(*n, sep='\n')
