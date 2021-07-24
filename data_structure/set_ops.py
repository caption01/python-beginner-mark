course_a = {'James', 'Brook', 'Kath', 'Mark', 'Peter', 'Anad'}

course_b = {'Sadie', 'Suresh', 'Simon', 'Peter', 'Greg', 'Kath'}

# Student who took both course
intersect = course_a & course_b
print(f'Took both course: {intersect}')

# Student from both course
union = course_a | course_b
print(f'All student: {union}')

# Student who took only one course
sym_diff = course_a ^ course_b
print(f'Took only one course {sym_diff}')