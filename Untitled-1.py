import random

grid= [[0 for col in range(4)]
                    for row in range(5)]
print(grid)
for _ in range(2):
    random_index = random.randrange(len(grid))
    random_inner_list = grid[random_index]
    random_item_index = random.randrange(len(random_inner_list))
    replacement_item = random.choices([2, 4], weights=[0.9, 0.1])[0]

    random_inner_list[random_item_index] = replacement_item

def merge():
    'print the grid in a vertical way'
    for col in range(4):
        for row in range(5):
            print(grid[row][col], end=' ')
        print()

merge()

#choose index randomly from grid
