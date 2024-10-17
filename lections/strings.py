"====================Строки================"
#21.08.24
#Строки - неизменяемый тип данных, который предназначен для хранения текста
#(любой поледовательности символов), заключенного в одинарные или двойные кавычки


# string1 = 'hello'
# string2 = "world"
# #error_Str = 'hello world" так нельзя
# str3 = "don't"
# str4 = 'don\'t'
# #print(str3) don't
# #print(str4) don't
# str5 = "'ada courses'"
# #print(str5) 'ada courses' внутри двойных все одинарные просто символы
# str6 = '"hello"'
# #print(str6) "hello" внутри одинарных все двойные просто символы
# str = """
# многострочный текст в тройных кавычках, тут можно ставить "Любые" 'кавычки'   """

# #конкатинация - склеивание строк
# string = 'hello'
# string3 = 'world'
# #print(string + '' + string3) hello world
# string4 = 'hello' + '' + 'world'
# # print(string4) hello world
# string5 = 'ADA'
# #print(string5 * 100) ADA 100 times
# "================Экранизация строк==================="
# # '\n' - Перенос на новую строку
# # print('hello\nworld\nwhy\ndoes\nshe') hello
# #                                       world
# #                                       etc.
# #print('hello\tworld\twhy\tdoes\tshe') hello   world   why     does    she
# #print('hello\'worldwhy') hello'worldwhy
# '====================Форматирование строк================='
# # name_of_model = input('Введите название модели: ')
# price_iphone14 = 1000
# price_iphone15 = 1100
# price_iphone15_pro = 1250

# #1 способ - f-строки
# # string = f'Название модели: {name_of_model}\nЦена товара:{price_iphone14}'
# # print(string)
# #2 способ 
# format1 = 'название модели: {}\nЦена товара: {}'
# # print(format1.format(name_of_model, price_iphone14))
# format3 = 'Название модели: %s\nЦена товара: %s'
# # print(format3 % (name_of_model, price_iphone14))

# '================Методы строк=============='
# #методы - функции, которые относятся к определенному типу данных, к ним мы обращаемся через точку

# #dir()- функция которая выводит все методы, которые относятся к определенному типу данных
# # print(dir('hello'))

# # .lower() - метод который переводит всю строку в нижний регистр
# string1 = 'hHLREOWFello wWORLFOrld'
# print(string1.lower())
# print('HELLO'.lower())

# #.upper - метод который переводит всю строку в верхний регистр

# print(string1.upper())
# print('hello'.upper())

# # .swapcase() - метод который переводит все символы в противоположнвй регистр
# print(string1.swapcase())
# #title()- меняет первую на заглавную
# string = 'hello world my name is denizkhan'
# print(string.title()) # Hello World My Name Is Denizkhan

# #.capitalize() - делает первую букву в строке заглавной
# string = 'hello world my name is denizkhan'
# print(string.capitalize())

# #.count - считает кол-во определенных символов
# string = 'hello world my name is denizkhan'
# print(string.count('l'))
# .startswith() - проверяет, начинатеся ли исходная строка с введенной подстроки
# возвращает булевое значение
# string_ = 'hello world my name is denizkhan!'
# print(string_.startswith('hello')) #True

# # .endswith проверяет, заканчивается ли исходная строка с введенной подстроки
# # возвращает булевое значение

# print(string_.endswith('denizkhan!')) # True

# string_ = 'hello'
# # .islower() - проверяет является ли строка полностью в нижнем регистре
# # возвращает булевое значение
# print(string_.islower()) # True

# # .isupper()- проверяет является ли строка полностью в верхнем регистре
# # возвращает булевое значение
# string_ = 'HELLO'
# print(string_.isupper()) # True

# # .isdigit() - проверяет состоит ли строка полностью из символов
# str_ = '12345'
# print(str_.isdigit()) # True

# # .isalpha() - проверяет состоит ли строка полностью из букв
# str_ = 'aboubakar'
# print(str_.isalpha()) # True

# # .isalnum() - проверяет состоит ли строка из символов или букв
# str_ = '12fujmkd131'
# print(str_.isalnum()) # True

# # .split() - разделяет строку по указанному разделителю, если его не указать то разделит по пробелу
# # Возвращает список
# string = 'hello world this is ada courses'
# print(string.split('i'))
# list_str = string.split()

# #.join() - принимает список из строк и соединяет их в одну, по указанному символу 
# list_str = string.split()
# print('='.join(list_str))

# #.strip() - убирает пробелы справа и слева строки
# str = '                    rij ggslk gm                    '
# print(str.strip())

# # .lstrip() - убирает пробелы слева
# str = '                    rij ggslk gm                    '
# print(str.lstrip())
# # .rstrip() - убирает пробелы справа
# str = '                    rij ggslk gm                    '
# print(str.rstrip())

# '===========Индексы==========='
# # индекс - это порядковый номер элемента в последовательности ()
# 'h e l l o w o r l d'
# #0 1 2 3 4 5 6 7 8 9 10
# string1 = 'ada courses'
# print(string1[5])
# list_ = ['ada', 'courses', 'bishkek', '21.08']
# print(list_[0])

# 22.08.24
# .startswith() - проверяет, начинатеся ли исходная строка с введенной подстроки
# возвращает булевое значение    

"============Срезы============"
# срез - подстрока строки


string = 'hello world this is ada courses'
print(string[0:11]) # hello world
print(string[12:]) # this is ada courses
print(string[0::2]) #
print(string[0::-1]) 
