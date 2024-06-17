from sys import stdin
from re import subn

flag = True

for i in stdin:

    result = subn(r'^"""', '', i.strip())
    if result[1]:
        flag = False

    result_2 = subn(r'.+"""$', '', i.rstrip())
    if result_2[1]:
        flag = True
        continue

    if subn(r'^(\s+)?#.+', '', i.rstrip())[1]:
        continue

    result_3 = subn(r'#.+', '', i.rstrip())
    if flag:
        print(result_3[0])
