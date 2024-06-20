from re import compile

reg = compile(r'\d+')
pos, endpos = input().split()

result = 0
result += sum(int(i) for i in reg.findall(input(),
                                          pos=int(pos),
                                          endpos=int(endpos)))

print(result)