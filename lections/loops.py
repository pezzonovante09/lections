# '=================Циклы================='
# Цикл - это блок кода, который отрабатывает несколько раз
# for - цикл, который работает с итерируемыми объектами, цикл заканчивает свою работу, когда он доходит до последнего элемента
#while - циел, который работает до тех пор пока услове верное(возвращает True)

# list1 = ['hello world', 1, 2, 3, True, None, [1, 2, 3]]
# for i in list1:
#     print(i)
# for letter in 'hello world':
#     print(letter)


# n = 1
# while n <= 10:
#     print(n)
#     n +=1
# # 1 2 3 4 5 6 7 8 9 10


# n = 1
# while n:
#     print('hello')
    # 0 - False                1 - True

'==============ключевые слова в циклах================='
# break - полностью останавливает цикл
# continue - пропускает одну итерацию, и переходит сразу к следующей

# for i in range(10):
#     if i == 3:
#         continue
#     print(i)
# # 0 1 2 4 5 6 7 8 9

# for i in range(10):
#     print(i)
#     if i == 3:
#         continue
# # 0 1 2 3 4 5 6 7 8 9

# for i in range(10):
#     print(i)
#     break
# # 0

# for i in range(10):
#     print(i)
#     if i == 5:
#         break



# list1 = [1, 2, 3, 1, 1, 3, 5, 1, 3]
# new_list = []

# for num in list1:
#     if num == 1:
#         continue
#     new_list.append(num)

# while 1 in list1:
#     list1.remove(1)
# print(list1)

# for i in range(10):
#     print(i, 'i')
#     for j in range(10):
#         print(j, 'j')
n = []
for i in range(21):
    if i % 2 == 0:
        n.append(i)
print(n)


