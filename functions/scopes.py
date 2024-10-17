'=========================Области видимости==========================='
# LEGB - Local Enclosed Global Built in

'=========================Built in=============================='
# Встроенное пространство имен (list, sum, dict, print, input)

'=========================Global============================'
'''
Все переменные, которые мы создали внутри одного файла
Чтобы посмотреть все глобальные переменные, можно использовать функцию globals
'''

# a = 5
# b = 10
# print(globals())

'==========================Enclosed==========================='
# Замкнутое пространство имен - локальное пространство, у которого есть внутреннее локальное пространство

# var = 'global'

# def func():
#     '''
#     Локальное пространство для глобального пространства
#     Замкнутое пространство (потому что есть более локальное пространство)
#     '''
#     var = 'enclosed'
#     def inner_func():
#         # Локальное пространство для пространства функции func()
#         var = 'local'
#         print(var)
#     print(var)
#     inner_func()

# print(var)
# func()
# global  
# enclosed
# local

'=======================Local====================='
# Локальное пространство имен - переменные, созданные внутри функции

# a = 10

# def func(a, b):
#     print('GLOBALS', globals())
#     print('LOCALS', locals())
#     print(a, b)

# func(10, 12)

# count = 1

# def increase_count():
#     global count
#     print(count)
#     count +=1

# increase_count()
# increase_count()
# increase_count()
# increase_count()


# def count(i):
#     counter = 0

#     def increase_count():
#         nonlocal counter
#         print(counter)
#         counter +=1
#     for j in range(i):
#         increase_count()

# count(100)


# def func():
#     local_var = 10

# func()
# # print(local_var) #NameError
# func()

'''
1) ИЗ ГЛОБАЛЬНОЙ ОБЛАСТИ ВИДИМОСТИ, ПОЛУЧИТЬ ДОСТУП К ПЕРЕМЕННЫМ ЛОКАЛЬНОЙ ОБЛАСТИ НЕВОЗМОЖНО

2) ИЗ ЛОКАЛЬНОЙ ОБЛАСТИ ВИДИМОСТИ ДОСТУП К ГЛОБАЛЬНОЙ ОГРАНИЧЕН ( ВЫ МОЖЕТЕ ЕЕ РАСПЕЧАТАТЬ, НО НЕ ИЗМЕНИТЬ, ДЛЯ ИЗМЕНЕ
НИЯ НУЖНА ФУНКЦИЯ global <НАЗВАНИЕ ПЕРЕМЕННОЙ>)

3) ИЗ ЛОКАЛЬНОЙ ОБЛАСТИ ВИДИМОСТИ ДОСТУП К ПЕРЕМЕННЫМ ЗАМКНУТОЙ ОБЛАСТИ ТАКЖЕ ОГРАНИЧЕН(ВЫ МОЖЕТЕ ЕЕ РАСПЕЧАТАТЬ
НО НЕ ИЗМЕНИТЬ, ДЛЯ ИЗМЕНЕНИЯ НУЖНО ИСПОЛЬЗОВАТЬ nonlocal <НАЗВАНИЕ ПЕРЕМЕННОЙ>)

'''

# 1 правило (пример)

# def function1():
#     count = 0 # Переменная локальной области видимости
#     print(count)

# print(count)

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# numbers1 = [a, b, c, d, e]
# numbers1.sort()
# print('Your set - ', set(numbers1))
# print('Lowest number - ', numbers1[0])

# import math

# credit = int(input('Your credit - '))
# if credit >= 100000:
#     credit1 = credit * 7.89
#     credit2 = round(credit1, 2)
#     print(credit2)
# else:
#     print('You can\'t take lower than 100000')


# import re
# a = 0
# text = str(input('Your text - '))
# numbers = re.findall(r'\d+', text)
# print(numbers)
# print(text)
# for i in numbers:
#     a += int(i)
# print(a)


# a = int(input('Months - '))
# b = int(input('Years - '))
# sum = 0
# def cube(months, years):
#     for i in range(1, months + 1):
#         global sum
#         sum += 30
#     for i in range(1, years + 1):
#         sum += 360
#     print(sum)

# cube(a, b)

# def cube():
#     a = {i: i ** 3 for i in range(1, 11)}
#     print(a)
# cube()

# def sum1():
#     a = 0
#     for i in range(50):
#         a +=i
#     print(a)
# sum1()
# def change(list1):
#     list1[0], list1[1] = list1[1], list1[0]
#     list1[2], list1[3] = list1[3], list1[2]

#     print(list1)
# change(['django', 'jork', 'brainrot', ' homelander'])
import random

def gen_number():
    str1 = 312
gen_number()






