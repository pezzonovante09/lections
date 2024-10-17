'=====================Функции================='
# функции - это наименованый блок кода, который может принимать аргументы
#  и возвращать результат

def my_sum(a, b):
    return a + b

res = my_sum(1,56)
print(res)

def my_len(obj):
    count = 0
    for i in obj:
        count +=1 # инкремент
    return(count)
print(my_len([1,2,3,4,5,6,7,10]))

'''
ФУНКЦИИ СОБЛЮДАЮТ ПРИНЦИП DRY(don't repeat yourself)
'''

'===================Аргументы и параметры========================='
'''
параметры - это переменные внутри функции, значения которым мы задаем при вызове функции
(т.е. те переменные, которые мы пишем в круглых скобках, когда пишем def)

аргументы - значения, которые мы передаем при вызове функции
'''

'========================Виды параметров====================='
# 1) обязательные
# 2) необязательные
# 2.1) с дефолтным значением(со значением по умолчанию)
# 2.2) args(все позиционные аргументы, которые не попали в обязательные, и с дефолтом)
# 2.3) kwargs(все лишние именованые аргументы)

'================================Виды аргументов==================================='
# 1) позиционные (по позиции)
# 2) именованые (по названию (параметр=значение))

# def add_or_add_10(num1, num2=10):
#     '''
#     Складывает 2 числа, если 2 число не передать, сложит первое с 10
#     '''
#     return num1 + num2
# num = 100
# print(add_or_add_10(num))

# '=========================*======================='
# list1 = list(range(1, 11))
# print(list1) # [1,2,3,4,5,6,7,8,9,10]
# list2 = [*range(1,11)]
# print(list2) # [1,2,3,4,5,6,7,8,9,10]
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# list3 = [*dict1]
# dict2 = {**dict1}
# print(dict2)
# print(list3)

# def fun(a, b=10, *args, **kwargs):
#     print('a -', a)
#     print('b - ', b)
#     print('args - ', args)
#     print('kwargs - ', kwargs)

# fun(b=100, a=12)

'====================Lambda==================='
# lambda - анонимная функция, которая записывается в одну строку
# lambda_func = lambda x: x ** 10
# print(lambda_func(10))

'====================Калькулятор======================'

# calc = {
#     '+': lambda n1,n2: n1 + n2,
#     '-': lambda n1,n2: n1 - n2,
#     '*': lambda n1, n2: n1 * n2,
#     '**': lambda n1, n2: n1 ** n2,
#     '/': lambda n1, n2: n1 / n2,
#     '//': lambda n1, n2: n1 // n2,
#     '%': lambda n1, n2: n1 % n2
# }
# def main():
#     try:
#         num1 = int(input('First number - '))
#         num2 = int(input('Second number - '))
#         operation = input('Operation - ')
#         func = calc[operation]
#         result = func(num1, num2)
#         print(num1, operation, num2, '=', result)

#     except ValueError:
#         print('Write number!')
#     except KeyError:
#         print('Operation incorrect')
#     except ZeroDivisionError:
#         print('You can\'t divide by 0')

# while True:
#     main()
#     if input('End? (yes/no) ').lower().strip() == 'yes':

db = [
    {'name': 'Nikita', 'password': hash('12345678')},
    {'name': 'hello', 'password': hash('hello world')}
]
def in_database(name):
    for user in db:
        if user['name'] == name:
            return True
    return False

def register(name, password1, password2):
    if in_database(name):
        raise Exception('User with this name, aleady existing!')
    if password1 != password2:
        raise Exception('Passwords are not equal!')
    user = {'name': name, 'password': hash(password1)}
    db.append(user)
    print(db)
    return 'You\'ve successfully registred'

def login(name, password):
    if not in_database(name=name):
        raise Exception('User is not existing!')
    for user in db:
        if user['name'] == name:
            if user['password'] != hash(password):
                raise Exception('Password is incorrect!')    
    return 'You successfully logined'

from decorators import time_decorator

@time_decorator

def main():
    print('Welcome!')
    while True:
        try:
            action = input('Register:1, Login:2, Quit:3\n')

            if action == '3':
                break
            elif action == '1':
                name = input('Write your name: ')
                p1 = input('Write your password: ')
                p2 = input('Repeat your password: ')
                print(register(name=name,password1=p1,password2=p2))
            elif action == '1':
                name = input('Your name: ')
                password = input('Your password: ')
                print(login(name=name,password=password))
            else:
                print('Incorrect choose!')
        except Exception as error:
            print(error)
    
main()