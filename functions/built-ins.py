'==========================Встроенные функции======================'
# map, zip, filter, enumerate

'''
zip - функция, которая соединяет несколько последовательностей 
(получаем генератор, в котором элементы - tuple)
'''

# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c']
# list3 = [10.5, 20.6, 30.8, 23,12]
# zipped = zip(list1, list2, list3)
# for element in zipped:
#     print(element) 

# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c', 'd', 'e']
# dict_ = dict(zip(list1, list2))
# print(dict_) # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

'''
enumerate - нумерует последовательность (по дефолту с 0) (также получаем генератор)
'''

enumerated = enumerate('hello')
print(enumerated) # <enumerate object at 0x0000024DC719DA80>
for i in enumerated:
    print(i)
# (0, 'h')
# (1, 'e')
# (2, 'l')
# (3, 'l')
# (4, 'o')

string = 'hello world'
print(list(enumerate(string[5:])))

'''
map - принимает функцию и последвательность (записывает в новую последовательность результат функции
,в которую передаются элементы последовательности)
'''

list1 = ['1', '2', '3', '4', '5']
mapped = list(map(int, list1))
print(mapped)

string = 'hello world'
res = ''.join(map(lambda x: x.upper(), string))
print(res)

list1 = [1, 2, 3, 4, 5]
res = list(map(lambda x: x ** 2, list1))
print(res)

def to_2_degree(x):
    return x ** 2

print(list(map(to_2_degree, list1)))

'''
filter - возвращает генератор, с элементами, прошедшими фильтр (какое- то условие),
принимает функцию и последовательность
'''

# list1 = [3, -5, -10, 0, 1, 2, 3, 4, 5, -100]
# filtered_List = list(filter(lambda x: x > 0, list1))
# print(filtered_List)

# users = [
#     {'name': 'Nastya', 'age':22}
#     {'name': 'Nikita', 'age':14}
#     {'name': 'Marat', 'age':17}
# ]
# result = list(filter(lambda x: x['age']>15, users))

'''
reduce - принимает функцию и последовательность, возвращает 1 результат
(передаваемая функция должна принимать 2 аргумента), оборачивать в list/dict не нужно и нельзя
'''

list1 = [1, 2, 3, 4, 5]
from functools import reduce
res = reduce(lambda x, y: x + y, list1)
print(res)

string = 'hello'
res = reduce(lambda x, y: x + '%' + y, string)
print(res)