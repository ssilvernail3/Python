# List Comprehensions

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# evens = []
# for num in nums:
#     if num % 2 == 0:
#         evens.append(num)

# print(evens)

# evens = [num for num in nums if num % 2 == 0]

# [num * 2 for num in nums]

# [what_to_add for thing in list ] this is the syntax for comprehensions what we want to add to the list,
# followed by some 'thing' in a specific 'list'

# evens = [2, 4, 6, 8]
# [num ** 2 for num in evens]

# [char.upper() for char in ['lmfao']]

# [num for num in range(10,20)]

def gen_board(size, initial_val=None):
    return[[initial_val for x in range(size)] for y in range(size)]


[x * 2 for x in range(10) if x % 2 == 0]

chickens = [
    {'name': 'Henry', 'sex': 'Rooster'},
    {'name': 'Lady Gray', 'sex': 'Hen'},
    {'name': 'Junior', 'sex': 'Rooster'},
    {'name': 'Stevie Chicks', 'sex': 'Hen'},
    {'name': 'Rocket', 'sex': 'Hen'},
    {'name': 'Butters', 'sex': 'Rooster'},
]

hens = [bird['name'] for bird in chickens if bird['sex'] == 'Hen']

scores = [55, 89, 99, 87, 60, 70, 74, 76, 90, 50, 82]
# grades = ['PASS' for score in scores if score >= 70]


# for adding an else to a comprehension
# [do_this if something else do this for thing in list]
# reads as:  do the first thing if something is true else do this other thing for an item in a list

grades = ['PASS'if score >= 70 else 'FAIL' for score in scores]
