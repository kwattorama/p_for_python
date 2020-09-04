'''PRINT THE NESTED LIST ELEMENTS'''
# given = ['ABC', [5, 5.4, 'XA'], 'xyz', None]
# for idx in given[1]:
#     print(idx)


'''if kwatt is present in the given list then print 'i am kwatt' '''
# given = ['xai', 'pranali', 'shivam', 'nimesh', 'kwatt']
# for idx in given:
#     if idx == 'kwatt':
#         print('i am kwatt')


'''print the below sequence using tuple starting from 2 and having 20 elements
2 * 4 = 8
3 * 5 = 15
4 * 6 = 24
..........
..........'''

# numbers = (tuple(range(2, 22)))
# print(len(numbers), '\n')

# for idx, idy in enumerate(numbers, start=4):
#     print(idy, '*', idx, '=', (idy * idx))


'''form a tuple having values upto 25, print the first 5 numbers'''
# tuple_2 = tuple(range(1, 26))
# idx = 1
# while idx <= tuple_2[4]:
#     print(idx)
#     idx += 1


'''print the all values of key-'job' with their sequence number'''

# given = {'name': 'shivam', 'job': ('doc', 'engg', 'gamer', 'teacher')}
# for idx, profession in enumerate(given['job'], start=1):
#     print(idx, profession)


'''Print the values of the inner dict(nested dict) with their sequence number'''

# given = {'name': 'CR07', 'job': {'doc': 'house', 'True': False, 'teacher': 'book'}}
# new_dict = given['job']
# print(new_dict)
# print(new_dict.values(), '\n')

# for idx, number in enumerate(new_dict.values(), start=1):
#     print(idx, number)
