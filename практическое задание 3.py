month = int(input('Введите номер месяца от 1 до 12: '))

year_dict = {
    1: 'январь', 2: 'февраль', 3: 'март',
   4: 'апрель',    5: 'май',    6: 'июнь',
    7: 'июль',    8: 'август',    9: 'сентябрь',
    10: 'октябрь',    11: 'ноябрь',    12: 'декабрь'
}
month_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
    'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

if month in month_list:      #не могу понять почему код не видит и list?
    print(f'{month}-й месяц это - {month_list[month - 1]}')
elif month in year_dict:
    print(f'{month}-й месяц это - {year_dict[month]}')
else:
    print('Вы должны были ввести месяц от 1 до 12')

#winter_list = ['декабрь', 'январь', 'февраль']
#spring_list = ['март', 'апрель', 'май']
#summer_list = ['июнь', 'июль', 'август']
#autumn_list = ['сентябрь', 'октябрь', 'ноябрь']
#while month <1 or month >12:
#    month = int(input('Введите номер месяца от 1 до 12: '))
#if month == 12 or month == 1 or month == 2:
#    print('Зима')
#elif month == 3 or month == 4 or month == 5:
#    print('Весна')
#elif month == 6 or month == 7 or month == 8 :
#    print('Лето')
#elif month == 9 or month == 10 or month == 11:
#    print('Осень')