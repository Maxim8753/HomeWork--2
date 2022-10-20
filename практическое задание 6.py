goods = []
goods_param_dict = {'название: ': '', 'цена: ': '', 'количество: ': ''}
analitics_dict = {'название: ': [], 'цена: ': [], 'количество: ': []}
num = 0

while True:
    if input('для выхода Quit, для продолжения Enter: ').upper() == 'Quit':
        break
    num += 1
    for goods_price in goods_param_dict.keys():
        goods_input = input(f'Введите {goods_price}')
        goods_param_dict[goods_price] = int(goods_input) \
            if goods_price in ('цена: ','количество: ') else goods_input
        analitics_dict[goods_price].append(goods_param_dict[goods_price])
    goods.append((num, goods_param_dict))
    print(f'      Товары: \n{goods}')
    print(f"      Аналитика товаров\n{'-' * 30}")
    for key, value in analitics_dict.items():
        print(f'{key[:20]:>15}:{value}')
    print('-' * 30)
