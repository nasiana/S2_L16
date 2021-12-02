"""
TOURNAMENT WINNER EXAMPLE SOLUTION
"""

# Test cases -- winner is 'Dolphins'
from typing import List

competitions = [
    ['Panthers', 'Lionesses'],
    ['Lionesses', 'Dolphins'],
    ['Dolphins', 'Panthers'],
]

results = [0, 0, 1]

comp_res = list((competitions [i], results[i]) for i in range(len(results)))
list_winner = []
for i in comp_res:
    if i[1] == 1:
        winner = i[0][0]
    elif i[1] == 0:
        winner = i[0][1]
    list_winner.append(winner)


most_common = max(list_winner, key = list_winner.count)
print('The winner is {}'.format(most_common))


#######################################################

# Test cases -- winner is 'D'

competitions = [
    ['A', 'B'],
    ['B', 'C'],
    ['C', 'A'],
    ['D', 'C'],
    ['E', 'D'],
    ['D', 'A'],
]

results = [0, 1, 1, 1, 0, 1]

comp_res = list((competitions [i], results[i]) for i in range(len(results)))
list_winner = []
for i in comp_res:
    if i[1] == 1:
        winner = i[0][0]
    elif i[1] == 0:
        winner = i[0][1]
    list_winner.append(winner)


most_common = max(list_winner, key = list_winner.count)
print('The winner is {}'.format(most_common))

#######################################################

# Test cases -- winner is 'Lionesses'

competitions = [
    ['Panthers', 'Lionesses'],
    ['Panthers', 'Dolphins'],
    ['Dolphins', 'Lionesses'],
]

results = [0, 0, 0]

comp_res = list((competitions [i], results[i]) for i in range(len(results)))
list_winner = []
for i in comp_res:
    if i[1] == 1:
        winner = i[0][0]
    elif i[1] == 0:
        winner = i[0][1]
    list_winner.append(winner)


most_common = max(list_winner, key = list_winner.count)
print('The winner is {}'.format(most_common))



#######################################################