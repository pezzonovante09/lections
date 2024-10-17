# numbers
# int - целые числа

# # type - тип данных

# # int - превращает в int

# # c = int('10')
# # print(type(c)) # 10


# # float - десятичные числа
# float = 15.4
# print (0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1)        

# #decimal - точное десятичное число
# # чтобы использовать десимал надо импортировать
# from decimal import Decimal
# a = Decimal('0.1')
# print(a + a + a + a+a+a+a+a+a+a)

# num1 = int(input('first number: '))
# num2 = int(input("second number: "))
# operation = input('operation: ')
# a = 0
# while True:
#     if operation == '/':
#         print(num1/num2)
#     elif operation == '+':
#         print(num1+num2)
#     elif operation == '-':
#         print(num1-num2)
#     elif operation == '*':
#         print(num1*num2)
#     elif operation == '%':
#         print(num1%num2)
#     elif operation == '**':
#         print(num1**num2)
#     elif operation == '//':
#         print(num1//num2)
#     else:
#         print("Данной операции нет в системе")
# #     b = input("Хотите ли вы продолжить? ")
# #     if b != 'yes':
# #         break

# while True:
#     num1 = int(input('first number: '))
#     num2 = int(input("second number: "))
#     operation = input('operation: ')
    
#     if operation == '/':
#         print(num1 / num2)
#     elif operation == '+':
#         print(num1 + num2)
#     elif operation == '-':
#         print(num1 - num2)
#     elif operation == '*':
#         print(num1 * num2)
#     elif operation == '%':
#         print(num1 % num2)
#     elif operation == '**':
#         print(num1 ** num2)
#     elif operation == '//':
#         print(num1 // num2)
#     else:
#         print("Данной операции нет в системе")
    
#     b = input("Хотите ли вы продолжить? (yes/no) ").strip().lower()
#     if b != 'yes':
#         break

# print('До свидания')

#pow()
#1. возводит число в степень (первоче число в скобках это то число которое нужно возвести в степень,
#  а второе число это степень в которую возведем число)
print(pow (2, 3)) # 8
# 2. находит остаток от деления на 3 число
print(pow(2,3,3)) # 2
print(2 ** 3 % 3) # 2

#divmod - функция которая возвращает 2 числа 1 - целая часть от деления 2 число  - остаток от деления
print(divmod(5, 2)) # (2, 1)
print(divmod(17, 3)) # (5, 2)
print((3 ** 1989) % 7)





