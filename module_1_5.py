immutable_var = 1, 'String', False
print(immutable_var)
#immutable_var[2]=True - 'tuple' object does not support item assignment
#print(immutable_var) - Объект «Кортеж» не поддерживает назначение элементов
mutable_list=[1,2,3,'String', True]
print(mutable_list)
mutable_list[0]=33
print(mutable_list)
mutable_list=mutable_list+["Modified"]
print(mutable_list)
