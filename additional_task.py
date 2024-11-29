grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list=list(students)
print('Список студентов: ',students_list)
sorted_list=sorted(students_list)
print('Список студентов в алфавитном порядке: ',sorted_list)
#grades[0]=sum(grades[0])/len(grades[0])
#grades[1]=sum(grades[1])/len(grades[1])
#grades[2]=sum(grades[2])/len(grades[2])
#grades[3]=sum(grades[3])/len(grades[3])
#grades[4]=sum(grades[4])/len(grades[4])
#print('Средний балл: ',grades)
for i in range(len(grades)):
    grades[i]=sum(grades[i])/len(grades[i])
print('Средний балл: ',grades)
average_ball={sorted_list[0]:grades[0],sorted_list[1]:grades[1],sorted_list[2]:grades[2],sorted_list[3]:grades[3],sorted_list[4]:grades[4]}
#average_ball=dict(zip(sorted_list,grades))
print('Средний балл студентов: ',average_ball)
