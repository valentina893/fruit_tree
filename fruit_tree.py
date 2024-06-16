import random

print('Come and shake the magical fruit tree!')

fruits = ['apple', 'orange', 'banana', 'strawberry', 'mango', 'grapefruit', 'blueberry', 'peach']

Program = True

while Program:
    user_input = input().lower()
    if user_input == 'shake':
        selection = random.choice(fruits)
        fruits.remove(selection)
        print('A', selection, 'has fallen from the tree!')
    else:
        print('Goodbye.')
        Program = False
    if len(fruits) == 0:
        print('The tree is no more! You were too selfish.')
        Program = False