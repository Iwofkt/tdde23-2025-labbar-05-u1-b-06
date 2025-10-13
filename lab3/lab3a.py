#A program where you can do operations on a board with pieces

def new_board():
    return {}

# Check if a coordinate is free from pieces
def is_free(board, x, y):
    return (x, y) not in board

# Place a piece on the board
def place_piece(board, x, y, player_key):
    if is_free(board, x, y):
        board[(x, y)] = player_key
        return True

    return False


# Get the player at a specific coordinate
def get_piece(board, x: int, y: int):
    return board.get((x, y), False)


# Remove a piece from the board
def remove_piece(board, x, y):
    if is_free(board, x, y):
        return False

    del board[(x, y)]
    return True

# Move one piece from one place to another
def move_piece(board, x1, y1, x2, y2):
    player_key = get_piece(board, x1, y1)
    if not player_key:
        return False
    if remove_piece(board, x1, y1):
        if place_piece(board, x2, y2, player_key):
            return True

        # If unable to put piece in new position, put back piece to original position
        place_piece(board, x1, y1, player_key)
    return False

# Count all pieces a player has on one row or column
def count(board, direction, position, player):
    amount = 0
    for (x, y), owner in board.items():
        if owner == player:
            if (direction == "row" and y == position) or (direction == "column" and x == position):
                amount += 1

    return amount

# Find the nearest piece to a coordinate
def nearest_piece(board, x, y):
    min_value = float("inf")
    chosen_piece = None

    for (px, py), player_key in board.items():
        #Pythagoras giving the differance squared
        difference = abs(x - px)**2 + abs(y - py)**2

        if difference < min_value:
            min_value = difference
            chosen_piece = (px, py)

    return chosen_piece if chosen_piece else False
