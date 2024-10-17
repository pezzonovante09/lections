# "=====================Логические и условные операторы======================"
# #22.08.24
# #логические операторы - выражения, которые возвращают True если выражение верное
# # и False - если не верное  
# 'Равенство'
# 5 == 5
# # = - присваивание значения
# # == - сравнение

# 'Неравенство'
# # 5 != 5

# 'больше'
# # 5 > 6

# 'меньше'
# # 5 < 6

# 'юольше или равно'
# # 5 >= 5

# 'меньше или равно'
# # 5 <=10
# '==================And or Not=============='
# # and - требует чтобы 2 выражения были верными
# #or - требует чтобы хотя бы 1 выражение было верным
# #not

# a = 5
# b = 6
# print(a == 5 and b ==6) # True

# # or
# # если хоть 1 часть выражения вернет true окончательно будет true
# print( a == 5 or b == 100) # True

# # not
# print(not a == 5) # False

# '======================Boolean type===================='
# # булевый тип данных имеет всего 2 значения true или false
# print(bool(1)) # True
# print(bool(0)) # False
# print(bool('hello')) # True
# print(bool([]))

# '==============Условные операторы================='
# # условные операторы это конструкция которая используется для того
# #  чтобы при разных входных данных код работал по разному(в зависимости от условия)

# a = 5
# b = 6
# if a < b:
#     print('ya ochumec my eto znaem my vmeste zazhigaem')


'===================Тернарные операторы===================='
#тернарные операторы это условие в одну строку

# тело1 if условие else тело2

# num = int(input())
# res = 'hello' if num == 5 else 'Bye'
# print(res)
# print('hello' if num == 5 else 'Bye')

# num = int(input())
# if num % 3 == 0 and num % 5 == 0:
#     print('Fizz')
# elif num % 3 == 0:
#     print('Buzz')
# elif num % 5 == 0:
#     print('FizzBuzz')
# else:
#     print(num)

# num = int(input())

# if num % 15 == 0:
#     print('FizzBuzz')
# elif num % 3 == 0:
#     print('Buzz')
# elif num % 5 == 0:
#     print('FizzBuzz')
# else:
#     print(num)

# num = int(input())

# if not num % 15:
#     print('fizzbuzz')
# elif not num % 3:
#     print('Fizz')
# elif not num % 5:
#     print( 'Buzz')
# else:
#     print(num)