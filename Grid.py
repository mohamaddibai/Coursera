
GRID_HEIGHT = 4
GRID_WIDTH = 6

# Create a rectangular grid using nested list comprehension 
# Inner comprehension creates a single row
EXAMPLE_GRID = [[ 0 for col in range(GRID_WIDTH)]
                           for row in range(GRID_HEIGHT)]

print(EXAMPLE_GRID)