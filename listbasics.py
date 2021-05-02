# to illustratre list basics utilities

courses = ['history', 'math', 'physics','CompSci']
courses_2 = [ 'polity', 'education']
nums = [1, 5, 2, 4, 3]
print(courses) # print list
print(len(courses)) # print len of list 4 (0-3)
print(courses[0])  # print first element of list
print(courses[3])
print(courses[-1]) # print last element of list
print(courses[0:2]) # print selected list starts from 0 end to 2(excluded)
print(courses[2:]) # slicing
courses.append('art') #add art at end
courses.insert(0, 'Art') # add at specific position
courses.extend(courses_2)
courses.remove('history') # it will remove particular element
courses.pop()  # it will remove from last of the list
# pop returns the value it pops so we can use it like to save wat is popped
courses.reverse() # to reverse the list
courses.sort()
nums.sort() # to sort in ascending
nums.sort(reverse=True)
sorted_courses = sorted(courses) # to get the sorted vesion of list in another variable
print(min(nums)) # min
print(max(nums)) # max element
print(sum(nums)) # sum of all elements
print(courses.index('art'))
# simple for loop traversal
for course in courses:
    print(course)
# for enumerated for loop traversal with indexing
for index, course in enumerate(courses): # to start with one just add enumerate(courses ,start=1)
    print(index, course)
# to make list like string
course_str = ' - '.join(courses)
print(course_str)
# to make list from string or undo the above task
new_list = course_str.split(' - ')
print(new_list)
print(nums)
print(courses)