'''Given a two integer numbers return their product
 and
if the product is greater than 1000, then return their sum'''

# num_1 = float(input("Enter first number: "))
# num_2 = float(input("Enter second number: "))
# mul = num_1 * num_2
# if mul > 1000:
#     print(f"sum of numbers is {num_1 + num_2}")
# else:
#     print(f"product of numbers is {mul}")
''' 


Q.4} Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string'''

# word = input("Enter the word>>> ")
# number = int(input("Enter the number>>> "))

# if len(word) > number:
#     print(word[number:])
# else:
#     print("number is greater than length of string")

'''
Q.5} Given a list of numbers, return True if first and last number of a 
list is same.
Given list is  [10, 20, 30, 40, 10],
 Given list is  [10, 20, 30, 40, 50]
 '''
# numbers = [10, 20, 30, 80, 0, 10]

# if numbers[0] == numbers[-1]:
#     print("result is True")
# else:
#     print("result is False")


'''
Question 6: Given a list of numbers, Iterate it and print only those
numbers which are divisible of 5
'''
# numbers = list(range(51))

# for idx in numbers:
#     if idx % 5 == 0:
#         print(idx)


'''
Q.7} Return the total count of sub-string “Emma” appears in the given string
Given string is “Emma is good developer. Emma is a writer”

Expected Output:
Emma appeared 2 times
'''
# given = "Emma is good developer. Emma is a writer"
# print(f"Emma appeared {given.count('Emma')} times")

'''
Question 8: Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
'''
# count = 0
# number = range(1, 6)

# for idx in number:
#     count += 1
#     print(str(idx) * count)
