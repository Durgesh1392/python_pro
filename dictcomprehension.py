# x,y,z,n=1,1,1,2
# my_list = [ (i, j) for i in range(x+1) for j in range(y+1)]
# print(my_list)
# for i in range(1):
#     print(i)
# Dictionary comprehension
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Deadpool']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
#print(zip(names, heroes))
l = zip(names, heroes)
list_1 = list(l)
# print(list_1)
# I want a dict {'name':'hero'} for each name, hero in zip(names, heros)
# my_dict = {}
# for name, hero in list_1:
#     my_dict[name] = hero
# print(my_dict)

my_dict = {name: hero for name , hero in list_1 if name != 'Peter'}
print(my_dict)
