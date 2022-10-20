data_list = [12, True , 'Hello', 3.14]

print(type(data_list))
print(type(data_list[0]))
print(type(data_list[1]))
print(type(data_list[2]))
print(type(data_list[3]))
for i, item in enumerate(data_list,1):
    print(f' {i} {data_list[i - 1]}')
