# # '====================Comprehensions========================'
# # #генератор,с помощью которого мы можем создавать последовательности используя
# # #цикл for В одну строку

# # '''
# # Cинтаксис:

# # рещультат for элемент in последовательность
# # результат for элемент in последовательность if филтр
# # '''

# # comprehension = (i for i in range(1, 6))
# # print(comprehension)
# # # генератор - это итерируюемаый обЪект который не хранти в себе полностью всю последовательность данных
# # # а создает когда требуется

# # print(next(comprehension))
# # print(next(comprehension))
# # print(next(comprehension))
# # print(next(comprehension))
# # print(next(comprehension))

# # '================list comprehension=============='
# # list_comprehension = list(1 ** 2 for i in range(1, ))
# # print(list_comprehension)

# # list_comprehension1 = [i ** 2 for i in range(1, 6)]

# # list_comprehension2 = [i ** 2 for i in range(1, 10) if i % 2 == 0]

# # list2 = ['hello' for i in range(5)]
# # list = ['hello', 'hello', 'hello', 'hello', 'hello']
# # list1 = ['hello'] * 5
# # print(list1)

# list1 = []
# for i in range(1, 11):
#     list1.append('четное') if i % 2 == 0 else list1.append('нечетное')
# print(list1)

# list3 = ['hello', 'python', 1, 2, {1: 'a'}, [1,2,3], ' world']
# list_comprehension5 = [i for i in list3 if type(i) == str]
# print(list_comprehension5)

# '=======================Dict Comprehensions=========================='
# dict1 = {i: i**2 for i in range(1, 11)}
# dict2 = {key: value for key, value in dict1.items()}
# dict3 = {value: key for key, value in dict1.items()}

# dict1 = {"a": [1, 2, 3, 4],
#     "b": [10,111,222,333],
#     "c": [1, 2, 543]}

# dict2 = {key: sum(value) for key, value in dict1.items()}
# print(dict2)

# dict4 = {i:f'{i}' for i in range(1,11)}
# print(dict4)

# list1 = [1, 2, 3, 4, 5]
# list2 = ['a', 'b', 'c', 'd', 'e']

# # dict1 = {}
# # for index in range(len(list1)):
# #     key = list1[index]
# #     value = list2[index]
# #     dict1[key] = value

# # print(dict1)  

# dict1 = {list1[index]: list2[index] for index in range(len(list1))}
# print(dict1)
# dict3 = dict(zip(list1, list2))
# print(dict3)

# "=======================Вложенные comprehension========================"
# dict1 = {}
# for i in range(1, 6):
#     key = i
#     value = [j for j in range(1, i + 1)]
#     dict1[key] = value
# print(dict1)

# dict2 = {i: [j for j in range(1, i +1)] for i in range(1, 6)}
# print(dict2)

# #                04.09.24
# # 1)

# # for i in range(1, 11):
# #     inner_list = []
# #     for j in range(5):
# #         inner_list.append('hello')
# #     list1.append(inner_list)

# # print(list1)


# # list1 = [['hello'] * 5 for i in range(10)]
# # print(list1)

# # list2 = [['hello world' for j in range(5)] for i in range(10)]
# # print(list2)

# # list1 = [['hello world'] * 5] * 10
# # print(list1)

# list1 = [[i for i in range(1, 6)] for j in range(10)]
# print(list1)

# dict1 = {}
# for i in range(1, 6):
#     inner_dict = {}
#     for j in range(1, i +1):
#         list_ = []
#         for k in range(1 , j + 1):
#             list_.append(k)
#         inner_dict[j] = list_
#     dict1[i] = inner_dict
# print(dict1)

# dict1 = {
#     i:{
#         j:[k for k in range(1, j + 1)] for j in range(1, i + 1)
#     }
#     for i in range(1, 6)
# }
# print(dict2)

# dict3 = {i: {j: list(range(1, j + 1)) for j in range(1, i + 1)} for i in range(1, 6)}
# print(dict3)

# dict1 = {"sedan": 1500, 'SUV':2000, 'pickup': 2500, 'minivan':1600, 'vann':2400,'semi':13600,'bicycle':7,'motorcycle':110}
# dict2 = {k.replace('i', ''): k.count('i') for k in dict1}
# print(dict2)

dict_ = {
    'Dasha': {
        'likes': 15,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
        ],
        'rating': 2
    },
    'Luna': {
        'likes': 12,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
        ],
        'rating': 1
    },
    'Rena': {
        'likes': 26,
        'comments': [
            {'id': 1, 'text': 'some text'},
            {'id': 2, 'text': 'some text'},
            {'id': 3, 'text': 'some text'},
            {'id': 4, 'text': 'some text'},
            {'id': 5, 'text': 'some text'},
            {'id': 6, 'text': 'some text'},
        ],
        'rating': 2
    }
}

list_id = []
for inner_dict in dict_.values():
    comments = inner_dict['comments']
    if len(comments) > 3:
        for comment in comments:
            list_id.append(comment['id'])
print(list_id)

lsd = [comment['id'] for inner_dict in dict_.values() if len(inner_dict['comments']) > 3 for comment in inner_dict['comments']]
print(lsd)

























































































































































































































































































































































































































































































































































































































































