my_dict={'Ivan':1989,'Anton':1988,'Dmitryi':1996}
print("Dict: ",my_dict)
print('Existing value: ',my_dict['Ivan'])
print('Not existing value: ',my_dict.get('Liza'))
my_dict.update({'leila':1966,'ilya':1985})
print('Updated value: ',my_dict)
a=my_dict.pop('Anton')
print('Deleted value: ',a)
print('Last version: ', my_dict)
my_set={1,2,2,3,3,(1,2,3),'set','set',True}
print('Set: ', my_set)
print(my_set.add(5))
print(my_set.add('new'))
print(my_set.remove(3))
print('Modified set: ',my_set)