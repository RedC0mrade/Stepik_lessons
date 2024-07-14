emails = [input().split('@')[0] for _ in range(int(input()))]
names = [input() for _ in range(int(input()))]
n = '@beegeek.bzz'
for a in names:
    if a in emails:
        count = 1
        while a in emails:
            a = a.rstrip('1234567890')
            a += str(count)
            count += 1
        emails.append(a)
        print(f'{a}{n}')
    else:
        emails.append(a)
        print(f'{a}{n}')