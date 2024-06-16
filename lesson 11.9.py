from re import sub


text = 'Ba-Ba-Ba-Ba-Barbara Ann'

print(sub(r'\b(\w+)(\W+\1\b)+', r'\1', text))