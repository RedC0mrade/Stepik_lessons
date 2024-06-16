from re import findall, subn, split


def funk(match):
    n = split(r'\(|\)', match.group())
    return n[1] * int(n[0])


text = 'bbbb10(2(a))bbb'

while '(' in text:


print(subn(r'\d+\(\w+\)', funk, text))



