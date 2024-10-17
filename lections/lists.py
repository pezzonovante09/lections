'=====================List===================='
#списки - это изменяемый, индексируемый, упорядоченный, итерируемый тип данных,
#который предназначен для хранения любых данных в определенном порядке


# list = [1, 2, 3, 4, 5, True, False, [1,2,3], {'a': 1}, [[(1,2,3)]]]
# print(list[-1][-1]) # 3
# print(list[-1][-1][-1])

# list1 = list('hello')
# list3 = list(range(11))
# print(list3)

# list4 = [1] * 5
# print(list4)

'===============================Методы списков==============================='
# append() - добавляет элемент в конец списка
# list2 = []
# list2.append(1)
# list2.append(454)
# list2.append(True)
# list2.append([1, 'hello'])
# print(list2)

#pop() - удаляет элемент из списка по индексу и результатом метода будет удаленный элемент
#если не передать индекс он автоматом удалит элемент с конца

# del_element = list2.pop(0)
# print(list2, del_element)
# element = list2.pop()
# print(element)
# print(list2)


# #remove() - удаляет элемент по значению
# list_= [True, False, 1, 2, 3]
# list_.remove(True)
# print(list_)
# list_.remove(3)
# print(list_)

# #count() - считает кол - во принятого элемента в списке
# list_ = [1, 1, 1, 1, 1, 2 ,3 ,4 ,5]
# print(list_.count(1))

# #index() - возвращает индекс первого вхождения принятого элемента
# list_ = ['hello', 'hello', 'hello', 1, 2, 3, [1, 2, 3, True], (True, False, 23)]
# print(list_.index('hello'))
# print(list_.index(1))

# #extend - расширяет список новым списком
# list5 = [1,2,3]
# list6 = [4,5,6]
# list5.extend(list6)
# print(list5) # [1, 2, 3, 4, 5, 6]

# sort() - сортирует список состоящий из элементов одного типа данных
# list3 = [414, 41 ,4 ,513, 151, 123, -312 ,0 ,41]
# list3.sort()
# print(list3)

# # clear() - очищает список
# list3.clear()
# print(list3)

# list1 = [1, 2, 3, [4, 5, [6, 7, 8]]]
# print(len(list1))
# a, b, c = 1, 2, 3
# print(a)#1
# print(b)#2
# print(c)#3

a, b, c = ['Nikita', 'bishkek', 'kyrgyzstan']
print(a)
# print(b)
# print(c)

# list_ = [100, 200, 232, 329, 1000]
# result = list_[0] + list_[-1]
# print(result)

# list1 = [1, 2, 3, 4, 5]
# # x = int(input("number: "))
# # found = False
# # found = True if list_.count(x) > 0 else found = False
# #print(found)
# #print(x)
# #print(list_.index(x))
# list_ = [f'искомое число = {num}' for num in list1 if num == num]

list = [0, 10, 0, 25, 0, 0, 0]
n = 0
while list.count(0) > 0:
    if list[n] == 0:
        list.pop(n)
        print(list)
    else:
        n+=1
print(list)

print('hi there')
