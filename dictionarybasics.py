student = {'name':'john','age':25,'courses': ['math','compsci'] }

print(student)
print(student['courses'])
#print(student['phone']) # key error if it is not available
print(student.get('name'))
print(student.get('phone', 'not found'))

# to add in dictionary
student['phone'] = '555-5555'

#update
student.update({'name':'jane','age':26,'phone':'555-5555'})
print(student)
# del keyword
# del student['age']
print(student)
age = student.pop('age')
print(age)
print(len(student))
print(student.keys()) # for keys
print(student.values())
print(student.items()) # for both key and values
# loop through dictionary
for key in student:
    print(key)

for key, value in student.items():
    print(key, value)
