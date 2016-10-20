from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Vamos a jugar batalla naval!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print ship_row
print ship_col

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):
    print "Turn", turn + 1
    guess_row = int(raw_input("Adivina la fila:"))
    guess_col = int(raw_input("Adivina la columna:"))

    if guess_row == ship_row and guess_col == ship_col:
        print "Felicidades! Hundiste mi barco!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, eso no esta en el oceano"
        elif(board[guess_row][guess_col] == "X"):
            print "Ese ya lo habias adivinado!"
        else:
            print "Hundiste mi barco!"
            board[guess_row][guess_col] = "X"
        # Print (turn + 1) here!
        print_board(board)

    if turn == 3:
        print "Perdiste"
