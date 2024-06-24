from re import split


def cal(b, kb, mb, gb):
    if b > 512:
        kb += round(b / 1024)
    if kb > 512:
        mb += round(kb / 1024)
    if mb > 512:
        gb += round(mb / 1024)
    if gb:
        return f'Summary: {gb} GB'
    if mb:
        return f'Summary: {mb} MB'
    if kb:
        return f'Summary: {kb} KB'
    if b:
        return f'Summary: {b} B'


dict_of_result = {}
with open(r'files.txt', 'r', encoding='UTF-8') as file:
    for i in file:
        stroka = split(r'[\s|\.]', i.rstrip())
        dict_of_result.setdefault(stroka[1], []).append(stroka)

dict_of_result = dict(sorted(dict_of_result.items()))
for i in dict_of_result:
    dict_of_result[i] = sorted(dict_of_result[i])
    b = sum(int(j[2]) for j in dict_of_result[i] if j[3] == 'B')
    kb = sum(int(j[2]) for j in dict_of_result[i] if j[3] == 'KB')
    mb = sum(int(j[2]) for j in dict_of_result[i] if j[3] == 'MB')
    gb = sum(int(j[2]) for j in dict_of_result[i] if j[3] == 'GB')

    for k in dict_of_result[i]:
        print(f'{k[0]}.{k[1]}')
    print('-' * 10)
    print(cal(b, kb, mb, gb))
    print()