from pprint import pprint

def read_input(input_file):

    with open(input_file) as f:

        lol = []
        for line in f:
            lol.append([e for e in line.rstrip()])

    return lol



def get_surrounding_elements(i, j):

    surrounding_elements = [
        (i - 1, j), # top
        (i - 1, j + 1), # top right
        (i, j + 1), # right
        (i + 1, j + 1), # bottom right

        (i + 1, j), # bottom
        (i + 1, j - 1), # bottom left
        (i, j - 1), # left
        (i - 1, j - 1), # top left
    ]

    return surrounding_elements


def part1():

    grid = read_input('day4/input.txt')

    rows = len(grid)
    columns = len(grid[0])

    # Iterate through every coordinate of the grid

    xmas_string_coords = []
    for i in range(rows):
        for j in range(columns):

            # If we find an 'X', search every direction for an 'M', 
            if grid[i][j] == 'X':

                x_surrounding_elements = get_surrounding_elements(i, j)
                for element_x in x_surrounding_elements:
                    try: 
                        
                        if grid[element_x[0]][element_x[1]] == 'M':
                            # Capture the direction that 'M' is in...
                            # print('X: ', i, j)
                            # print('M: ',element_x[0], element_x[1])
                            
                            # This is the direction of travel to see if we can find A, S...
                            diff = (element_x[0] - i, element_x[1] - j)
                            # print(diff)

                            try:
                                if (element_x[0] + diff[0] < 0) or (element_x[1] + diff[1] < 0):
                                    continue
                                if grid[element_x[0] + diff[0]][element_x[1] + diff[1]] == 'A':
                                    print('A: ',element_x[0] + diff[0], element_x[1] + diff[1])
                                    

                                    try:
                                        if (element_x[0] + diff[0] + diff[0] < 0) or (element_x[1] + diff[1] + diff[1] < 0):
                                            continue
                                        if grid[element_x[0] + diff[0] + diff[0]][element_x[1] + diff[1] + diff[1]] == 'S':
                                            xmas_string_coords.append(
                                                [
                                                    (i,j),
                                                    (element_x[0], element_x[1]),
                                                    (element_x[0] + diff[0], element_x[1] + diff[1]),
                                                    (element_x[0] + diff[0] + diff[0], element_x[1] + diff[1] + diff[1])
                                                ]
                                            )

                                    except IndexError:
                                        pass

                            except IndexError:
                                pass

                    except IndexError:
                        continue
            
            else:
                continue
    
    print(len(xmas_string_coords))
    # pprint(xmas_string_coords)


def part2():

    grid = read_input('day4/input.txt')

    rows = len(grid)
    columns = len(grid[0])

    xMas_coords = []

    # Iterate through every coordinate of the grid
    for i in range(rows):
        for j in range(columns):

            # Find an A
            if grid[i][j] == 'A':

                # If we go outside grid boundaries, skip
                if (i - 1 < 0) or (j - 1 < 0) or (j + 1 > columns - 1) or (i + 1 > rows - 1):
                    continue

                # Check every diagonal
                surrounding_letters = [
                    grid[i - 1][j - 1], # top left
                    grid[i - 1][j + 1], # top right
                    grid[i + 1][j + 1], # bottom right
                    grid[i + 1][j - 1], # bottom left
                ]

                # If the diagonal letters follow any of these patterns
                # it will make the X-MAS pattern we seek
                if surrounding_letters in [
                    ['M', 'S', 'S', 'M'],
                    ['M', 'M', 'S', 'S'],
                    ['S', 'M', 'M', 'S'],
                    ['S', 'S', 'M', 'M'],
                ]:
                    
                    # Found a match, record the coords to a list
                    xMas_coords.append(
                        [
                            (i,j), # center
                            (i - 1, j - 1),
                            (i - 1, j + 1),
                            (i + 1, j + 1),
                            (i + 1, j - 1),
                        ]
                    )

    pprint(xMas_coords)
    print(len(xMas_coords))
                



if __name__ == '__main__':

    part1()
    part2()