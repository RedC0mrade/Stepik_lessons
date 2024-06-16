from re import sub


text = 'beegeek,beegeek,beegeek! python python.. Python.. stepik?stepik?stepik'

print(sub(r'\b(\w+)(\W+\1?\b)+', r'\w+', text))