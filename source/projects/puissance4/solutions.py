import copy


def initialize_grid(n_rows=6, n_columns=7):
    grid = []

    for row in range(n_rows):
        empty_space_column = [' ' for space in range(n_columns)]
        grid.append(empty_space_column)
    return grid


def display_grid(grid):
    for row in grid:
        print("| " + " | ".join(row) + " |")


def make_move(grid, column_to_play, disc_color):
    grid = copy.deepcopy(grid)

    if grid[0][column_to_play] != " ":
        # If the chosen column has no empty space, raise an error
        raise ValueError(f"Column {column_to_play} is already full.")
    else:
        # Otherwise, go through the column from bottom to top until finding an empty space
        # Then place the disc in that space
        row = 5
        while grid[row][column_to_play] != ' ':
            row -= 1
        grid[row][column_to_play] = disc_color

    return grid


def check_row_victory(row):
    for i, elem in enumerate(row):
        # For each element in the row
        if elem in ["R", "Y"] and i + 3 <= len(row) - 1:
            # If the element is a disc and there are at least 3 elements to its right
            count_equal = 0
            for j in range(1, 4):
                # Count the number of discs of the same color to its right
                if elem == row[i+j]:
                    count_equal += 1
            if count_equal == 3:
                # If the counter is 3, it's a victory, the function returns True
                if elem == "R":
                    print("Red won!")
                if elem == "Y":
                    print("Yellow won!")
                return True
    return False


def check_horizontal_victory(grid):
    for row in grid:
        # Test the victory condition on each row
        if check_row_victory(row):
            return True
    return False


def check_vertical_victory(grid):
    for column_idx in range(7):
        # Get the elements of the column into a list
        column = []
        for row in grid:
            column.append(row[column_idx])
        if check_row_victory(column):
            # Test for the existence of a victory
            return True
    return False


def check_victory(grid):
    if check_horizontal_victory(grid) or check_vertical_victory(grid):
        return True
    return False


def make_move_and_check_victory(grid, column_to_play, disc_color):
    grid = copy.deepcopy(grid)
    grid = make_move(grid, column_to_play, disc_color)
    if check_victory(grid):
        print("GAME OVER")
    return grid
