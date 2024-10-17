# '================Модули и пакеты======================='
# # любой файл с расширением .py - модуль
# # пакет - набор модулей (обязательно должен быть файл __init__.py)

# '===============Работа с файлами============='
# # open - функция, которая открывает файл в определенном режиме
# '''
# РЕЖИМЫ:

# r - read (означает, что файл только для чтения)

# w - write (только для записи, каждый раз файл очищается)

# a - append (только для дозаписи, добавляется в конец)

# x - создает файл, но если он существует то выйдет ошибка

# b - binary (в бинарном виде)

# '''

# '================Read================'
# file = open('files/test.txt', 'r')
# print(dir(file))
# print(file.writable()) # False
# print(file.readable()) # True
# print(file.read())
# print(file.read()) # '' (потому что курсор находится)

# file.seek(0)
# print(file.read(5))

# file.seek(0)
# print(file.readline()) # gb410phj c891mu [19 (метод считывает только 1 строку)
# print(file.readline()) # ] moon tell me if i could (считывает 1 строчку потому что курсос перемещен)

# file.seek(0)
# print(file.readlines()) # (считывает все строки , и возвращает список из этих строк, добавляя в конец строки
# # \n - перенос на новую строку)

# file.close()

# '===============Write================'
# file2 = open('files/new_test.txt', 'w') 
# # если файла нет создаст автоматом
# # file2.write('Hello world\n')
# # file2.write('i love you soooooo, please let me go')
# # если были данные то они удаляются и записываются новые

# file2.writelines(['hello\n', 'world\n'])
# # метод writelines принимает список из строк, указываете \n если нужно перенести на новую строку

# file2.close()
# '================Append================='
# file3 = open('files/new_test.txt', 'a')
# file3.write('Oh i still wana be your favourite boooooooy i wanna be the one that makes you smile i wanna be the one')
# file3.seek(0)
# file3.write('GYAT') # все равно напишет в конец, даже если перенести в курсор
# file3.close()

# '=================Контекстный менеджер====================='
# with open('new_test.txt', 'r') as file4:
#     print(file4.read())
# print(file4.closed) # True
# # closed - проверяет закрыт ли файл и возвращает либо True, либо False

# #try:
# #   file = open('new_test.txt', 'r')
# #   file.write()
# #finally:
# #file.close

# file = open('files/task.txt', 'r')
# print(file.read())

# login = input('Write your login - ')
# password = input('Write your password - ')
# file1 = open('files/task.txt', 'a')
# file1.write(login)
# file1.write(password)

# file2 = open('files/task2.txt', 'r')
# if 'w' in file2.read():
#     print('Yes')
# else:
#     print('No')   

file3 = open('files/python.txt', 'r')
data = file3.read()
a = data.split()
o_words = []
for i in a:
    if 'o' in i:
        o_words.append(i)
print(o_words)


