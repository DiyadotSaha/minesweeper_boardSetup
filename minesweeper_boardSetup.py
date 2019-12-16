bomb_cordinates = []


def main():
    message = input('Enter the coordinates of the game board (ex. 2 4): ')
    r_c = message.split(' ')
    row, col = int(r_c[0]), int(r_c[1])
    num_bombs = input("Enter the number of bombs (ex. 3): ")
    global bomb_cordinates
    bomb_cordinates = bomb_coords(num_bombs)
    make_board(row, col)


def bomb_coords(num):
    list_cord = []
    num = int(num)
    for i in range(num):
        temp_list = input("Enter the coordinates of the bombs (ex. 1 0):").split(' ')
        temp_list = [int(temp_list[0]), int(temp_list[1])]
        list_cord += [temp_list]
    return list_cord


def make_board(r, c):
    for i in range(r):
        for j in range(c):
            if is_bomb(i, j) == True:
                if j == (c - 1):
                    print('*', end='')
                else:
                    print('*', end=' ')
            else:
                neigh = check_neighbours(i, j, r, c)
                if j == (c - 1):
                    print(neigh, end='')
                else:
                    print(neigh, end=' ')
        if i < (r - 1):
            print()


def is_bomb(i, j):
    b_list = bomb_cordinates
    checker = False
    for bomb in b_list:
        if i == bomb[0] and j == bomb[1]:
            checker = True
    return checker


def check_neighbours(r_cord, c_cord, R, C):
    neighbour = 0
    # for top left corner case
    if r_cord == 0 and c_cord == 0:
        if is_bomb(r_cord + 1, c_cord):
            neighbour += 1
        if is_bomb(r_cord + 1, c_cord + 1):
            neighbour += 1
        if is_bomb(r_cord, c_cord + 1):
            neighbour += 1
    # for bottom left corner case
    elif r_cord == R - 1 and c_cord == 0:
        if is_bomb(r_cord - 1, c_cord):
            neighbour += 1
        if is_bomb(r_cord - 1, c_cord + 1):
            neighbour += 1
        if is_bomb(r_cord, c_cord + 1):
            neighbour += 1
            # for top right corner case
    elif r_cord == 0 and c_cord == C - 1:
        if is_bomb(r_cord, c_cord - 1):
            neighbour += 1
        if is_bomb(r_cord + 1, c_cord - 1):
            neighbour += 1
        if is_bomb(r_cord + 1, c_cord):
            neighbour += 1
            # for bottom right corner case
    elif r_cord == R - 1 and c_cord == C - 1:
        if is_bomb(r_cord, c_cord - 1):
            neighbour += 1
        if is_bomb(r_cord - 1, c_cord - 1):
            neighbour += 1
        if is_bomb(r_cord - 1, c_cord):
            neighbour += 1
            # for the rightmost coloumn
    elif c_cord == C - 1:
        if is_bomb(r_cord - 1, c_cord):
            neighbour += 1
        if is_bomb(r_cord - 1, c_cord - 1):
            neighbour += 1
        if is_bomb(r_cord, c_cord - 1):
            neighbour += 1
        if is_bomb(r_cord + 1, c_cord - 1):
            neighbour += 1
        if is_bomb(r_cord + 1, c_cord):
            neighbour += 1
    # for the leftmost coloumn
    elif c_cord == 0:
        if is_bomb(r_cord - 1, c_cord):
            neighbour += 1
        if is_bomb(r_cord - 1, c_cord + 1):
            neighbour += 1
        if is_bomb(r_cord, c_cord + 1):
            neighbour += 1
        if is_bomb(r_cord + 1, c_cord + 1):
            neighbour += 1
        if is_bomb(r_cord + 1, c_cord):
            neighbour += 1
    # for the topmost row
    elif r_cord == 0:
        if is_bomb(r_cord, c_cord - 1):
            neighbour += 1
        if is_bomb(r_cord + 1, c_cord - 1):
            neighbour += 1
        if is_bomb(r_cord, c_cord + 1):
            neighbour += 1
        if is_bomb(r_cord + 1, c_cord + 1):
            neighbour += 1
        if is_bomb(r_cord + 1, c_cord):
            neighbour += 1
    # for the bottommost row
    elif r_cord == R - 1:
        if is_bomb(r_cord, c_cord - 1):
            neighbour += 1
        if is_bomb(r_cord - 1, c_cord - 1):
            neighbour += 1
        if is_bomb(r_cord - 1, c_cord):
            neighbour += 1
        if is_bomb(r_cord - 1, c_cord + 1):
            neighbour += 1
        if is_bomb(r_cord, c_cord + 1):
            neighbour += 1
    # for the middle box
    else:
        if is_bomb(r_cord, c_cord - 1):
            neighbour += 1
        if is_bomb(r_cord + 1, c_cord - 1):
            neighbour += 1
        if is_bomb(r_cord + 1, c_cord):
            neighbour += 1
        if is_bomb(r_cord + 1, c_cord + 1):
            neighbour += 1
        if is_bomb(r_cord, c_cord + 1):
            neighbour += 1
        if is_bomb(r_cord - 1, c_cord + 1):
            neighbour += 1
        if is_bomb(r_cord - 1, c_cord):
            neighbour += 1
        if is_bomb(r_cord - 1, c_cord - 1):
            neighbour += 1
    return neighbour


main()
