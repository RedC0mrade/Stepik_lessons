num = [int(i) for i in input().split()]

n=[]
for i in range(len(num)):
    if num[i] in num[i+1:] and num[i] not in n:
        n.append(num[i])
print(*sorted(n))