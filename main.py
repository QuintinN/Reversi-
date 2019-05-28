# Author: Quintin Nguyen
# Date: 04.12.19
# Description: Project 2, reversi game

# Global Variables
cpu = " O "
user = " X "


# Parameters: list; takes in a list such as the game board
# Return:    print; prints out the gameboard
def printBoard(board):
    # print header
    print("_| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |")

    # print each row
    # for example: 3|_|_|_|X|O|_|_|_|
    for i in range(len(board)):
        print(str(i) + "|" + "|".join(board[i]) + "|")


# Parameters: string; the playing tile
# Return:     string; string of the opposing piece
def getOpposingPiece(piece):
    global opposingPiece
    if piece == cpu:
        opposingPiece = user

    if piece == user:
        opposingPiece = cpu

    return opposingPiece


# Parameters: string; a string of the index of where I'm currently at on the board known as piece
#               list; of the board
#             string; a string of the opponent tile
# Return  :  boolean; of look that determines if the index up is checkable
def lookUp(piece, board, opponent):
    column = int(piece[1])
    rowCheck = int(piece[0]) - 1

    if rowCheck >= 0:
        charCheck = board[rowCheck][column]

        if charCheck == opponent:

            # Iterate upward the index being checked
            for i in range(rowCheck, -1, -1):

                char = board[i][column]

                if char != opponent and char != " _ ":  # means char = opponent piece
                    look = True
                    return look

                if char == " _ ":
                    look = False
                    return look

        if charCheck != opponent:
            look = False
            return look

    if rowCheck < 0:
        look = False
        return look


# Parameters: piece; a string of the index of where I'm currently at on the board
#             board; a list of the board
#          opponent; a string of the opponent
# Return    :  look; a boolean that determines if the index down is checkable
def lookDown(piece, board, opponent):
    column = int(piece[1])
    rowCheck = int(piece[0]) + 1

    if rowCheck < len(board):
        charCheck = board[rowCheck][column]

        if charCheck == opponent:

            # Iterates downward the index being checked
            for i in range(rowCheck, len(board), 1):

                char = board[i][column]

                if char != opponent and char != " _ ":
                    look = True
                    return look

                if char == " _ ":
                    look = False
                    return look

        if charCheck != opponent:
            look = False
            return look

    if rowCheck >= len(board):
        look = False
        return look


# Parameters: piece; a string of the index of where I'm currently at on the board
#             board; a list of the board
#          opponent; a string of the opponent
# Return    :  look; a boolean that determines if the index to the leftward is checkable
def lookLeft(piece, board, opponent):
    columnCheck = int(piece[1]) - 1
    row = int(piece[0])

    if columnCheck >= 0:
        charCheck = board[row][columnCheck]

        if charCheck == opponent:

            # Iterates leftward of the index being checked
            for i in range(columnCheck, -1, -1):
                char = board[row][i]

                if char != opponent and char != " _ ":
                    look = True
                    return look

                if char == " _ ":
                    look = False
                    return look

        if charCheck != opponent:
            look = False
            return look

    if columnCheck < 0:
        look = False
        return look


# Parameters: piece; a string of the index of where I'm currently at on the board
#             board; a list of the board
#          opponent; a string of the opponent
# Return    :  look; a boolean that determines if the index rightward is checkable
def lookRight(piece, board, opponent):
    columnCheck = int(piece[1]) + 1
    row = int(piece[0])

    if columnCheck < len(board):
        charCheck = board[row][columnCheck]

        if charCheck == opponent:

            # Iterates rightward of the index being checked
            for i in range(columnCheck, len(board), 1):
                char = board[row][i]

                if char != opponent and char != " _ ":
                    look = True
                    return look

                if char == " _ ":
                    look = False
                    return look

        if charCheck != opponent:
            look = False
            return look

    if columnCheck >= len(board):
        look = False
        return look


# Parameters: string; piece which is the player or cpu e.g. "X" and "O"
#             list;   board that is being played
# Return:     list;   string of all the possible moves that either player or cpu can play
def listValidMoves(piece, board):
    validMoves = []
    opponent = getOpposingPiece(piece)

    # Loop through each index of the board
    for row in range(len(board)):

        for column in range(len(board)):
            char = board[row][column]

            if char == " _ ":
                checkIndex = str(row) + str(column)
                checkUp = lookUp(checkIndex, board, opponent)
                checkDown = lookDown(checkIndex, board, opponent)
                checkLeft = lookLeft(checkIndex, board, opponent)
                checkRight = lookRight(checkIndex, board, opponent)

                validIndex = [row, column]

                if checkUp:
                    validMoves.append(validIndex)
                elif checkDown:
                    validMoves.append(validIndex)
                elif checkLeft:
                    validMoves.append(validIndex)
                elif checkRight:
                    validMoves.append(validIndex)

    return validMoves


# Parameters: list; calculated list of vaild moves a player can make
# Return:   string; valid move the player chose
def getMove(list):
    valid = False

    # Does not stop looping until user enters a valid input
    while not valid:

        user = input("Enter a move: ")
        user = user.strip()

        if len(user) == 3:
            row = user[0]
            column = user[2]
            user = "[" + row + ", " + column + "]"

            # Compare the user input to index's of list
            for i in range(len(list)):
                index = str(list[i])

                if index == user:
                    valid = True
                    return user

        print("Invalid move. Valid moves are: ", list)

    return valid


# Parameters: string; the piece that the user/cp is using
#             string; the index of the move
# Return:     list; updated list with the flipped pieces
def makeMove(pieceType, index, board):
    row = int(index[1])
    column = int(index[4])
    checkIndex = str(row) + str(column)
    opponent = getOpposingPiece(pieceType)

    checkUp = lookUp(checkIndex, board, opponent)
    checkDown = lookDown(checkIndex, board, opponent)
    checkLeft = lookLeft(checkIndex, board, opponent)
    checkRight = lookRight(checkIndex, board, opponent)

    board[row][column] = pieceType

    if checkUp:
        board = flipPiecesUp(pieceType, checkIndex, board)

    if checkDown:
        board = flipPiecesDown(pieceType, checkIndex, board)

    if checkLeft:
        board = flipPiecesLeft(pieceType, checkIndex, board)

    if checkRight:
        board = flipPiecesRight(pieceType, checkIndex, board)

    return board


# Parameters: string; the piece that user/cp is using
#             string; the index of the move
#               list; the old board with no flipped pieces
#
# Return:       list; the new board with flipped upward pieces
def flipPiecesUp(piece, index, board):
    row = int(index[0]) - 1
    column = int(index[1])

    # Flips the pieces until it reaches its own piece
    for i in range(row, -1, -1):
        char = board[i][column]

        if char != piece:
            board[i][column] = piece

        else:
            return board


# Parameters: string; the piece that user/cp is using
#             string; the index of the move
#               list; the old board with no flipped pieces
#
# Return:       list; the new board with flipped downward pieces
def flipPiecesDown(piece, index, board):
    row = int(index[0]) + 1
    column = int(index[1])

    # Flips the pieces until it reaches its own piece
    for i in range(row, len(board), 1):
        char = board[i][column]

        if char != piece:
            board[i][column] = piece

        else:
            return board


# Parameters: string; the piece that user/cp is using
#             string; the index of the move
#               list; the old board with no flipped pieces
#
# Return:       list; the new board with flipped leftward pieces
def flipPiecesLeft(piece, index, board):
    row = int(index[0])
    column = int(index[1]) - 1

    # Flips the pieces until it reaches its own piece
    for i in range(column, -1, -1):
        char = board[row][i]

        if char != piece:
            board[row][i] = piece

        else:
            return board


# Parameters: string; the piece that user/cp is using
#             string; the index of the move
#               list; the old board with no flipped pieces
#
# Return:       list; the new board with flipped rightward pieces
def flipPiecesRight(piece, index, board):
    row = int(index[0])
    column = int(index[1]) + 1

    # Flips the pieces until it reaches its own piece
    for i in range(column, len(board), 1):
        char = board[row][i]

        if char != piece:
            board[row][i] = piece

        else:
            return board


# Parameters: list; the cpu move
# Returns:  string; proper string of cpu move
def makeCpuMove(cpuMove):
    modifiedMove = "[" + str(cpuMove[0]) + ", " + str(cpuMove[1]) + "]"

    return modifiedMove


# Parameters: list; list of board
# Returns:  prints; a bunch of statements to call the game over
#           prints; final score between player and cpu
#               * but technically does not return anything
def getScore(board):
    print("GAME OVER")
    print("Current board state:")
    printBoard(board)

    userScore = 0
    cpuScore = 0

    # Iterate through the board list to count scores
    for row in range(len(board)):

        for column in range(len(board)):

            char = board[row][column]

            if char == user:
                userScore += 1

            if char == cpu:
                cpuScore += 1

    print("Player score: ", userScore)
    print("CPU score: ", cpuScore)

    if userScore > cpuScore:
        print("Player wins!")

    if cpuScore > userScore:
        print("CPU wins!")

    if userScore == cpuScore:
        print("Tie!")


def main():
    print("Current board state:")
    gameBoard = [[" _ ", " _ ", " _ ", " _ ", " _ ", " _ ", " _ ", " _ "],  # 0
                 [" _ ", " _ ", " _ ", " _ ", " _ ", " _ ", " _ ", " _ "],  # 1
                 [" _ ", " _ ", " _ ", " _ ", " _ ", " _ ", " _ ", " _ "],  # 2
                 [" _ ", " _ ", " _ ", " X ", " O ", " _ ", " _ ", " _ "],  # 3
                 [" _ ", " _ ", " _ ", " O ", " X ", " _ ", " _ ", " _ "],  # 4
                 [" _ ", " _ ", " _ ", " _ ", " _ ", " _ ", " _ ", " _ "],  # 5
                 [" _ ", " _ ", " _ ", " _ ", " _ ", " _ ", " _ ", " _ "],  # 6
                 [" _ ", " _ ", " _ ", " _ ", " _ ", " _ ", " _ ", " _ "]]  # 7

    printBoard(gameBoard)

    letsPlay = True

    while letsPlay:

        # Print possible user moves
        validMoves = listValidMoves(user, gameBoard)

        if len(validMoves) > 0:
            print("Valid moves are: ", validMoves)

            # Get a valid user move
            userMove = getMove(validMoves)
            print()

            # Update the board with flipped pieces from the users move
            gameBoard = makeMove(user, userMove, gameBoard)

        if len(validMoves) <= 0:
            getScore(gameBoard)
            letsPlay = False

        # Find possible moves for cpu
        validCpuMoves = listValidMoves(cpu, gameBoard)

        # Get cpu move if there are moves available
        if len(validCpuMoves) > 0:
            cpuMove = list(validCpuMoves[0])
            cpuMove = makeCpuMove(cpuMove)
            print("CPU takes move: ", cpuMove)

            # Update the board with flipped pieces from the cpu move
            print("Current board state:")
            gameBoard = makeMove(cpu, cpuMove, gameBoard)
            printBoard(gameBoard)

        # Ends game if there are no more cpu moves available
        if len(validCpuMoves) <= 0:
            getScore(gameBoard)
            letsPlay = False


main()
