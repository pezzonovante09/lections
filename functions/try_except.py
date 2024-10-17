'===============Exceptions==================='
# исключения (ошибки) - объекты,которые прерывают работу кода, если не были обработаны

SyntaxError
# исключение, которое выходит в случае, когда в коде допущена синтаксическая ошибка
# print(
# """
#   File "c:\Users\User\Desktop\lections\try_except.py", line 6
#     print(
#          ^
# SyntaxError: '(' was never closed  
# """

NameError
# исключение, которое выходит когда мы обращаемся к несуществующей переменной

# print(a)
#     print(a)
# NameError: name 'a' is not defined
# pezzonovante@DESKTOP-GPAOL64:/mnt/c/
IndexError
# list = [1, 2, 3, 4, 5]
# print(list[1000])
#IndexError: list index out of range

KeyError
# исключение, которое выходит, когда обращаемся к не существуемуюущу числу
# Dict_ = {'a': 1}
# print( dict_{b})
#     print( dict_{b})
#            ^^^^^^^^
# SyntaxError: invalid syntax. Perhaps you forgot a comma?

ValueError
# когда мы передаем в функцию не 

TypeError
# когда мы пытаемся использовать методы, не свойственные какому то типу данных 
# или когда пытаемся передать функции больше или меньше аргументов, чем принимает функция
 #for i in 123
#  File "/mnt/c/Users/User/Desktop/lections/try_except.py", line 40
   # for i in 123
#IndentationError: unexpected indent

#5 +'str'
#  File "/mnt/c/Users/User/Desktop/lections/try_except.py", line 45, in <module>
#     5 +'str'
# TypeError: unsupported operand type(s) for +: 'int' and 'str

# {[123]: "hello"}
#   File "/mnt/c/Users/User/Desktop/lections/try_except.py", line 50, in <module>
#     {[123]: "hello"}
# TypeError: unhashable type: 'list'

ZeroDivisionError
# выходит при делении на 0
# 45 / 0
#   File "c:\Users\User\Desktop\lections\try_except.py", line 57, in <module>
#     45 / 0
#     ~~~^~~
# ZeroDivisionError: division by zero

# 45 % 0
#   File "c:\Users\User\Desktop\lections\try_except.py", line 63, in <module>
#     45 % 0
#     ~~~^~~
# ZeroDivisionError: integer modulo by zero

# 45 // 0
#   File "c:\Users\User\Desktop\lections\try_except.py", line 69, in <module>
#     45 // 0
#     ~~~^^~~
# ZeroDivisionError: integer division or modulo by zero

IndentationError
# выходит, когда мы неправильно используем отступы

#    a = 5
#   File "c:\Users\User\Desktop\lections\try_except.py", line 78
#     a = 5
# IndentationError: unexpected indent

# for i in range(10):
# print(i)
#  File "c:\Users\User\Desktop\lections\try_except.py", line 84
#     print(i)
#     ^
# IndentationError: expected an indented block after 'for' statement on line 83

Exception
# исключение, которое создали, чтобы его вызвать

'============Вызов отношений============'
# raise NameError
# raise позволяет вручную вызывать исключение

#raise NameError('Нерпавильное имя пользователя')
#NameError: неправильное имя пользователя

'=================Обработка Исключений===================='
# чтобы код не прекращал работу когда возникает исключение, мы можем использовать
#конструкцию try-except, и обрабатывать вызванное исключение

# try:
#     # код, который возможно вызовет ошибку
#     num = int(input('Write a number - '))
# except ValueError: # ошибка которая может возникнуть
#    # Код который отрабатывает только если ошибка вызвалась
#    print('Write a number!')
# else:
#     # код, который отработает только если никакая ошибка не вышла
#     print('Your number - ', num)
# finally:
#     # код который отработает вообще в любом случае
#     print('До свидания')


# try:
#     raise ValueError
# except (SyntaxError, NameError): # exce[t не сработает потому что не передали ValueError в скобки
#     print('Вышла одна из этих ошибок: (SyntaxError, NameError)')

try:
    raise TypeError
except TypeError:
    print('Error is TypeError')


# try:
#    name = input('Your name - ')
#    country = input('Your country - ')
#    Year = int(input('Your birth year - '))
# except ValueError:
#    print('Incorrect!')
# else:
#    print(name)
#    print(country)
#    year2 = 0
#    for i in range(1, Year):
#       year2 = year2 + (Year % 10)
#       Year = Year // 10
#    print(year2)

# a = input('Your name - ')
# b = input('Your age - ')
# args1 = ()
# kwargs1 = {'name': a, 'age': b}


# def task(*args1, **kwargs):
#    print(kwargs['name'])
#    print(kwargs['age'])
# try:
#    task(name='nick', age= 23)
# except KeyError:
#    print('Incorrect!')


# def add(a, b):
#     print(a + b)
# def subtract(a, b):
#     print(a - b)
# def multiply(a, b):
#     print(a * b)
# def divide(a, b):
#     print(a / b)
# try:
#    a = int(input('First number - '))
#    b = int(input('Second number - '))
#    add(a, b)
#    subtract(a, b)
#    multiply(a, b)
#    divide(a, b)
# except ZeroDivisionError:
#     print('Incorrect')
# except ValueError:
#     print('Incorrect!')
l1 = [1, 4, 2, 4, 6, 1, 3]
l2 = [30, 10, 15]

def task5(l1, l2):
   try:
      for i in l1:
         a = l2[i]
         print(a)
   except IndexError:
      print('Incorrect!')
   

task5(l1, l2)
