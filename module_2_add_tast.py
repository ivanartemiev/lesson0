list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
password = []
while True:
    number = int(input("Введите число от 3 до 20: "))
    if number <= 20 and number >= 3:
        for i in list:
            for j in list:
                while True:
                    if number % (i+j) == 0  and i < j:
                        password += [i,j]
                        break
                    else:
                        break
        break
    elif number >= 20 or number <= 3:
        print('Вы не попали в числовой ряд!')
        continue
print('Ваш код пароль!')
for i in password:
    print(i, end='')


