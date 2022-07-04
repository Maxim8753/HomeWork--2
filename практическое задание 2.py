first_el = input('Введите первый элемент: ')
second_el = input('Введите второй элемент: ')
third_el = input('Введите третий элемент: ')
data_list_2 = [first_el, second_el,third_el]
print(data_list_2)

data_list_2.pop(1)
data_list_2.insert(0,second_el)
print(data_list_2)

data_list = [20, True, 'Hello', 'Пи = ']
data_list_1 = [22, False, 'World', 3.14]

Slise = data_list[:1] + data_list_1[:1]
Slise_1 = data_list[1:2] + data_list_1[1:2]
Slise_2 = data_list[2:3] + data_list_1[2:3]
Slise_3 = data_list[3:] + data_list_1[3:]

print(Slise)
print(Slise_1)
print(Slise_2)
print(Slise_3)

data_list.extend(data_list_1)
print(data_list)