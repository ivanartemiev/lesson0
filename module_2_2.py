first=input('Введите первое целое число: ')
second=input('Введите второе целое число: ')
third=input('Введите третье целое число: ')
if first == second and first==third and second==third:
    print('Количество одинаковых чисел: ',3)
elif first==second and first is not third or second == third and first is not third or first==third and second is not third:
    print('Количество одинаковых чисел: ',2)
else: print('Количество одинаковых чисел: ',0)