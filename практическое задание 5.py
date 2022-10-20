number_list = [7, 5, 3, 3, 2]
new_el = int(input('Введите новый элемент для рейтинга: '))
i = 0

for n in number_list:
    if new_el <=n:
        i +=1
    else:
        break
number_list.insert(i, new_el)

print(number_list)
print(max(number_list))