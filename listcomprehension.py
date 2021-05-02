num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# if i want to print list as it is
# my_list = []
# for n in num:
#     my_list.append(n)
# print("list is ", my_list)
# LIST COMPREHENSION
my_list = [ n for n in num]
print("list is ",my_list)

# if i want to print n*n in list
# my_list = []
# for n in num:
#     my_list.append(n*n)
# print(my_list)
#
# my_list = []
# my_list = [ n*n for n in num]
# print(my_list)

# if i want to print even number in list

my_list = []
for n in num:
    if n%2 == 0:
        my_list.append(n)
print(my_list)

# list comprehension
my_list = []
my_list = [ n for n in num if n%2 ==0]
print(my_list)

# if i want a (letter , num) pair for each letter in 'abcd' and each number in '0123'
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))
print(my_list)
# list comprehension
my_list = []
my_list = [ (letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)

