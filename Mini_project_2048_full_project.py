"""
Clone of 2048 game.
"""

# import poc_2048_gui
#import Mini_project_2048_unitTesting
import random
# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    user_list_input = line
    zero_list = [0] * len(user_list_input)
    saved = 0
    should_restart = True
    while should_restart:
        should_restart = False
        for value in enumerate(user_list_input):
            if value > 0:
                if value == saved :
                    zero_list[zero_list.index(saved)] = value + saved 
                    saved = 0
                    continue
                if value != saved:
                    zero_list[zero_list.index(0)] = value
                    saved = value
                    continue
        return zero_list


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.reset()
        self._up_indices = [(0, col) for col in range(self.grid_width)]
        self._down_indices = [(self.grid_height - 1, col) for col in range(self.grid_width)]
        self._left_indices = [(row, 0) for row in range(self.grid_height)]
        self._right_indices = [(row, self.grid_width - 1) for row in range(self.grid_height)]
        self._indices = {UP: self._up_indices,
                            DOWN: self._down_indices,
                            LEFT: self._left_indices,
                            RIGHT: self._right_indices}
        


    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        self._grid = [[0 for col in range(self.grid_width)]
                           for row in range(self.grid_height)]
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        print(self._grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self.grid_height
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self.grid_width
        
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        self.direction = direction
        if self.direction == UP:
            for cell in self._up_indices:
                self._grid[cell[0]][cell[1]] = merge(self.OFFSETS[direction])
        if self.direction == DOWN:
            for cell in self._down_indices:
                self._grid[cell[0]][cell[1]] = merge(self.OFFSETS[direction])
        if self.direction == LEFT:
            for cell in self._left_indices:
                self._grid[cell[0]][cell[1]] = merge(self.OFFSETS[direction])
        if self.direction == RIGHT:
            for cell in self._right_indices:
                self._grid[cell[0]][cell[1]] = merge(self.OFFSETS[direction])
        self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        for _ in range(2):
            random_index = random.randrange(len(self._grid ))
            random_inner_list = self._grid [random_index]
            random_item_index = random.randrange(len(random_inner_list))
            replacement_item = random.choices([2, 4], weights=[0.9, 0.1])[0]

            random_inner_list[random_item_index] = replacement_item

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self._grid[row][col] = value
    
    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._grid[row][col]

# poc_2048_gui.run_gui(TwentyFortyEight(4, 4))


def test_TwentyFortyEight():
    """
    Test code for TwentyFortyEight
    """
    
    my_game = TwentyFortyEight(5,4)
    my_game.reset()
    print("--------------------")
    my_game.__str__()
    print("--------------------")
    my_game.get_grid_height()
    print("--------------------")
    my_game.get_grid_width()
    print("--------------------")
    my_game.set_tile(1,1,7)
    print("--------------------")
    my_game.get_tile(1,1)
    print("--------------------")
    my_game.__str__()


    # add more tests here
    
test_TwentyFortyEight()
