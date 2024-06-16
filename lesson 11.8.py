from re import subn, split


def funk(match):
    n = split(r'\(|\)', match.group())
    return n[1] * int(n[0])


text = '1(a)b11(a)'

while '(' in text:
    text = subn(r'\d+\(\w+\)', funk, text)[0]

print(text)





