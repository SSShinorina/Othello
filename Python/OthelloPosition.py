import numpy as np
from OthelloAction import OthelloAction


class OthelloPosition(object):
    """
    This class is used to represent game positions. It uses a 2-dimensional char array for the board
    and a Boolean to keep track of which player has the move.

    For convenience, the array actually has two columns and two rows more that the actual game board.
    The 'middle' is used for the board. The first index is for rows, and the second for columns.
    This means that for a standard 8x8 game board, board[1][1] represents the upper left corner,
    board[1][8] the upper right corner, board[8][1] the lower left corner, and board[8][8] the lower left corner.

    Author: Ola Ringdahl
    """

    def __init__(self, board_str=""):
        """
        Creates a new position according to str. If str is not given all squares are set to E (empty)
        :param board_str: A string of length 65 representing the board. The first character is W or B, indicating which
        player is to move. The remaining characters should be E (for empty), O (for white markers), or X (for black
        markers).
        """
        self.BOARD_SIZE = 8
        self.maxPlayer = True
        self.board = np.array([['E' for col in range(self.BOARD_SIZE + 2)] for row in range(self.BOARD_SIZE + 2)])
        if len(list(board_str)) >= 65:
            if board_str[0] == 'W':
                self.maxPlayer = True
            else:
                self.maxPlayer = False
            for i in range(1, len(list(board_str))):
                col = ((i - 1) % 8) + 1
                row = (i - 1) // 8 + 1
                # For convenience we use W and B in the board instead of X and O:
                if board_str[i] == 'X':
                    self.board[row][col] = 'B'
                elif board_str[i] == 'O':
                    self.board[row][col] = 'W'

    def initialize(self):
        """
        Initializes the position by placing four markers in the middle of the board.
        :return: Nothing
        """
        self.board[self.BOARD_SIZE // 2][self.BOARD_SIZE // 2] = 'W'
        self.board[self.BOARD_SIZE // 2 + 1][self.BOARD_SIZE // 2 + 1] = 'W'
        self.board[self.BOARD_SIZE // 2][self.BOARD_SIZE // 2 + 1] = 'B'
        self.board[self.BOARD_SIZE // 2 + 1][self.BOARD_SIZE // 2] = 'B'
        self.maxPlayer = True

    def make_move(self, action, row=None, col=None, __has_neighbour=None):
        """
        Perform the move suggested by the OhelloAction action and return the new position. Observe that this also
        changes the player to move next.
        :param action: The move to make as an OthelloAction
        :return: The OthelloPosition resulting from making the move action in the current position.
        """
        # TODO: write the code for this method and whatever helper methods it need
        # action = []
        convert = []

        # For all the generated neighbours, determine if they form a line
        # If a line is formed, we will add it to the convert array
        for neighbour in __has_neighbour:
            neighX = neighbour[0]
            neighY = neighbour[1]
            # Check if the neighbour is of a different colour - it must be to form a line
            if action[neighX][neighY] != self.board[row][col]:
                # The path of each individual line
                path = []

                # Determining direction to move
                deltaX = neighX - row
                deltaY = neighY - col

                tempX = neighX
                tempY = neighY

                # While we are in the bounds of the board
                while 0 <= tempX <= 7 and 0 <= tempY <= 7:
                    path.append([tempX, tempY])
                    value = action[tempX][tempY]
                    # If we reach a blank tile, we're done and there's no line
                    if value == None:
                        break
                    # If we reach a tile of the player's colour, a line is formed
                    if value == self.board[row][col]:
                        # Append all of our path nodes to the convert array
                        for node in path:
                            convert.append(node)
                        break
                    # Move the tile
                    tempX += deltaX
                    tempY += deltaY

        # Convert all the appropriate tiles
        for node in convert:
            action[node[0]][node[1]] = self.board[row][col]

        return action

    def get_moves(self):
        """
        Get all possible moves for the current position
        :return: A list of OthelloAction representing all possible moves in the position. If the
        list is empty, there are no legal moves for the player who has the move.
        """
        moves = []
        append = moves.append
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                if self.__is_candidate(i + 1, j + 1) and self.__is_move(i + 1, j + 1):
                    append(OthelloAction(i + 1, j + 1))
        return moves

    def __is_candidate(self, row, col):
        """
        Check if a position is a candidate for a move (empty and has a neighbour)
        :param row: The row of the board position
        :param col: The column of the board position
        :return: True if it is a candidate
        """
        if self.board[row][col] != 'E':
            return False
        if self.__has_neighbour(row, col):
            return True
        return False

    def __is_move(self, row, col):
        """
        Check if it is possible to do a move from this position
        :param row: The row of the board position
        :param col: The column of the board position
        :return: True if it is possible to do a move
        """
        if row < 1 or row > self.BOARD_SIZE or col < 1 or col > self.BOARD_SIZE:
            return False
        if self.__check_north(row, col):
            return True
        if self.__check_north_east(row, col):
            return True
        if self.__check_east(row, col):
            return True
        if self.__check_south_east(row, col):
            return True
        if self.__check_south(row, col):
            return True
        if self.__check_south_west(row, col):
            return True
        if self.__check_west(row, col):
            return True
        if self.__check_north_west(row, col):
            return True

    def __check_north(self, row, col):
        """
        Check if it is possible to do a move to the north from this position
        :param row: The row of the board position
        :param col: The column of the board position
        :return: True if it is possible to do a move
        """
        if not self.__is_opponent_square(row - 1, col):
            return False
        i = row - 2
        while i > 0:
            if self.board[i][col] == 'E':
                return False
            if self.__is_own_square(i, col):
                return True
            i -= 1
        return False

    def __check_north_east(self, row, col):
        """
        Check if it is possible to do a move to the north east from this position
        :param row: The row of the board position
        :param col: The column of the board position
        :return: True if it is possible to do a move
        """
        if not self.__is_opponent_square(row - 1, col + 1):
            return False
        i = 2
        while row - i > 0 and col + i <= self.BOARD_SIZE:
            if self.board[row - i][col + i] == 'E':
                return False
            if self.__is_own_square(row - i, col + i):
                return True
            i += 1
        return False

    def __check_north_west(self, row, col):
        """
        Check if it is possible to do a move to the north west from this position
        :param row: The row of the board position
        :param col: The column of the board position
        :return: True if it is possible to do a move
        """
        if not self.__is_opponent_square(row - 1, col - 1):
            return False
        i = 2
        while row - i > 0 and col - i > 0:
            if self.board[row - i][col - i] == 'E':
                return False
            if self.__is_own_square(row - i, col - i):
                return True
            i += 1
        return False

    def __check_south(self, row, col):
        """
        Check if it is possible to do a move to the south from this position
        :param row: The row of the board position
        :param col: The column of the board position
        :return: True if it is possible to do a move
        """
        if not self.__is_opponent_square(row + 1, col):
            return False
        i = row + 2
        while i <= self.BOARD_SIZE:
            if self.board[i][col] == 'E':
                return False
            if self.__is_own_square(i, col):
                return True
            i += 1
        return False

    def __check_south_east(self, row, col):
        """
        Check if it is possible to do a move to the south east from this position
        :param row: The row of the board position
        :param col: The column of the board position
        :return: True if it is possible to do a move
        """
        if not self.__is_opponent_square(row + 1, col + 1):
            return False
        i = 2
        while row + i <= self.BOARD_SIZE and col + i <= self.BOARD_SIZE:
            if self.board[row + i][col + i] == 'E':
                return False
            if self.__is_own_square(row + i, col + i):
                return True
            i += 1
        return False

    def __check_south_west(self, row, col):
        """
        Check if it is possible to do a move to the south west from this position
        :param row: The row of the board position
        :param col: The column of the board position
        :return: True if it is possible to do a move
        """
        if not self.__is_opponent_square(row + 1, col - 1):
            return False
        i = 2
        while row + i <= self.BOARD_SIZE and col - i > 0:
            if self.board[row + i][col - i] == 'E':
                return False
            if self.__is_own_square(row + i, col - i):
                return True
            i += 1
        return False

    def __check_west(self, row, col):
        """
        Check if it is possible to do a move to the west from this position
        :param row: The row of the board position
        :param col: The column of the board position
        :return: True if it is possible to do a move
        """
        if not self.__is_opponent_square(row, col - 1):
            return False
        i = col - 2
        while i > 0:
            if self.board[row][i] == 'E':
                return False
            if self.__is_own_square(row, i):
                return True
            i -= 1
        return False

    def __check_east(self, row, col):
        """
        Check if it is possible to do a move to the east from this position
        :param row: The row of the board position
        :param col: The column of the board position
        :return: True if it is possible to do a move
        """
        if not self.__is_opponent_square(row, col + 1):
            return False
        i = col + 2
        while i <= self.BOARD_SIZE:
            if self.board[row][i] == 'E':
                return False
            if self.__is_own_square(row, i):
                return True
            i += 1
        return False

    def __is_opponent_square(self, row, col):
        """
        Check if the position is occupied by the opponent
        :param row: The row of the board position
        :param col: The column of the board position
        :return: True if opponent square
        """
        if self.maxPlayer and self.board[row][col] == 'B':
            return True
        if not self.maxPlayer and self.board[row][col] == 'W':
            return True
        return False

    def __is_own_square(self, row, col):
        """
        Check if the position is occupied by the player
        :param row: The row of the board position
        :param col: The column of the board position
        :return: True if it's your own square
        """
        if not self.maxPlayer and self.board[row][col] == 'B':
            return True
        if self.maxPlayer and self.board[row][col] == 'W':
            return True
        return False

    def __has_neighbour(self, row, col):
        """
        Check if the position has any non-empty squares
        :param row: The row of the board position
        :param col: The column of the board position
        :return: True if has neighbours
        """
        if self.board[row - 1][col] != 'E':
            return True
        if self.board[row - 1, col + 1] != 'E':
            return True
        if self.board[row - 1][col - 1] != 'E':
            return True
        if self.board[row][col - 1] != 'E':
            return True
        if self.board[row][col + 1] != 'E':
            return True
        if self.board[row + 1][col - 1] != 'E':
            return True
        if self.board[row + 1][col + 1] != 'E':
            return True
        if self.board[row + 1][col] != 'E':
            return True
        return False

    def to_move(self):
        """
        Check which player's turn it is
        :return: True if the first player (white) has the move, otherwise False
        """
        return self.maxPlayer

    def clone(self):
        """
        Copy the current position
        :return: A new OthelloPosition, identical to the current one.
        """
        ot = OthelloPosition("")
        ot.board = np.copy(self.board)
        ot.maxPlayer = self.maxPlayer
        return ot

    def print_board(self):
        """
        Prints the current board. Do not use when running othellostart (it will crash)
        :return: Nothing
        """
        print(self.board)
        # print("ToMove: ", self.maxPlayer)
