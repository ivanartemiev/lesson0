my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
#for i in range(len(my_list)):
    #while my_list[i] >= 0:
        #if my_list[i] >= 1:
            #print('Число положительно: ', my_list[i])
        #break
    #else:
        #break
#print('Конец программы!')
index = 0
while  my_list[index] >= 0 and index < len(my_list):
    if my_list[index] >= 1:
        print(my_list[index])
        index += 1
    else:
       index +=1
    continue
else:
    print('Конец программы!')