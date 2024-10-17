# '=====================Декораторы==================='
# # функция высшего порядка - функция, которая принимает в аргументы функцию, создает внутри себя
# # функцию, вызывает функцию и вовзращает функцию
# # декоратор - функция высшего порядка, которая нужна, чтобы расширять функционал функции не изменяя ее
# # (функция обертка)

# # def time_decorator(func):
# #     def wrapper(*args, **kwargs):
# #         from datetime import datetime
# #         start = datetime.now()
# #         func(*args, **kwargs)
# #         finish = datetime.now()
# #         print(f'Total time: {finish - start}')
# #     return wrapper
# # @time_decorator
# # def hello():
# #     print('hello world')
# # hello()
# # decorator = time_decorator(hello)
# # decorator()
# # @time_decorator
# # def my_sqrt(x):
# #     print(x ** 0.5)
    
# # my_sqrt(25)

# # def func_start_time(func):
# #     def wrapper(*args, **kwargs):
# #         from datetime import datetime
# #         now = datetime.now()
# #         correct_format = now.strftime('%d.%m.%Y %H:%M')
# #         print('Функция запущена', correct_format)
# #         func(*args, **kwargs)
# #     return wrapper
# # @func_start_time
# # def func():
# #     print('hello world')
# # func()

# def decorator(num):
#     def inner_decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(num):
#                 func(*args, **kwargs)
#         return wrapper
#     return inner_decorator

# @decorator(4)
# def hello():
#     print('hello world')
# hello()


# def decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result ** 2
#     return wrapper
# @decorator
# def multiply(a, b):
#     return a * b
# print(multiply(3, 4))


# def upper_case(func):
#     def wrapper(*args, **kwargs):
#         upperlist = func(*args, **kwargs)
#         return upperlist.upper()
#     return wrapper
# @upper_case
# def list1(l):
#     return l[-1]
# print(list1(['fnaofja', 'fiwofw', 'fiwofjwl']))

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         list_nums = func(*args, **kwargs)
#         set_nums = set(list_nums)
#         return list(set_nums)
#     return wrapper
# @decorator
# def random():
#     l1 = []
#     import random
#     for i in range(1, 101):
#         i = random.randint(10, 50)
#         l1.append(i)
#     return l1
# print(random())


# def decor(func):
#     def wrapper(*args, **kwargs):
#         hashed = func(*args, **kwargs)
#         return hash(hashed)
#     return wrapper
# @decor
# def log():
#     login = input('Your login - ')
#     password = input('Your password - ')
# print(log())

def dec(func):
    def wrapper(*args, **kwargs):
        with open('task12.txt', 'w') as file:
            data = func(*args, **kwargs)
            file.write(data)
        # return file.read
    return wrapper
@dec
def sum():
    return 'guf'
print(sum())
    


        
