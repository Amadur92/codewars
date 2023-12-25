"""DESCRIPTION:
Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]"""


def snail(snail_map):
    horizontal = list(range(len(snail_map[0])))
    vertical = list(range(len(snail_map)))
    current_pos = [0, 0]
    result = []
    while len(horizontal) > 0 and len(vertical) > 0:
        for i in horizontal:
            result.append(snail_map[current_pos[1]][i])
            current_pos[0] += 1
            print(current_pos)
        current_pos[0] -= 1
        snail_map.pop(current_pos[1])
        vertical = list(range(len(snail_map)))
        for j in vertical:
            result.append(snail_map[j][snail_map[current_pos[0]]])
            current_pos[1] += 1
            snail_map.pop(current_pos[j][-1])
        horizontal = list(range(len(snail_map[0])))
        horizontal.reverse()
        for i in horizontal:
            result.append(snail_map[current_pos[1]][i])
            current_pos[0] -= 1
            print(current_pos)
        current_pos[0] += 1
        snail_map.pop(current_pos[1])
        vertical = list(range(len(snail_map)))
        vertical.reverse()
        for j in vertical:
            result.append(snail_map[j][snail_map[current_pos[0]]])
            current_pos[1] -= 1
            snail_map.pop(current_pos[j][-1])
        horizontal = list(range(len(snail_map[0])))
    return result

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
print(snail(array))