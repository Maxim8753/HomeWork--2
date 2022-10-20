

user_words = input('Введите несколько слов через пробел: ').split()

for i, Slice in enumerate(user_words, 1):
    print(f'{i}) {Slice[:10]} ',sep = ':')
