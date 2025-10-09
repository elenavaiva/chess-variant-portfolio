# Author: Elena Vizgirdaite
# GitHub username: elenavaiva
# Date: 03/09/2025
# Description: Creating the King Of The Hills Chess Variant game.

class ChessVar:
    """Represents the King Of The Hills chess game variant"""
    def __init__(self):
            self._board = [
                 ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                 ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                 ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                 ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
                ]

            self._current_player = 'white'
            self._game_state = 'UNFINISHED'
            self._debug = False

    def get_game_state(self):
        """Returns the current state of the game ('UNFINISHED', 'WHITE_WON' or 'BLACK_WON')"""
        return self._game_state

    def get_board(self):
        """Returns the current state of the board in a form of the list"""
        return self._board

    def print_board(self):
        """Prints the board"""
        for i in range (0,len(self._board)):
            print(8-i, '|', ' | '.join(self._board[i]), '|')
        print('   ', '   '.join(['a','b','c','d','e','f','g','h']), ' ')

    def switch_player(self):
        """Switches the player according to whose turn it is"""
        if self._current_player == 'white':
            self._current_player = 'black'
        else:
            self._current_player = 'white'

    def get_square_i(self, square):
        """Returns a square of the board"""
        raw_row = square[1]
        row_i = 8 - int(raw_row)

        if row_i < 0 or row_i > 7:
            return -1, -1

        raw_col = square[0]

        if raw_col == "a":
            col_i = 0
        elif raw_col == "b":
            col_i = 1
        elif raw_col == "c":
            col_i = 2
        elif raw_col == "d":
            col_i = 3
        elif raw_col == "e":
            col_i = 4
        elif raw_col == "f":
            col_i = 5
        elif raw_col == "g":
            col_i = 6
        elif raw_col == "h":
            col_i = 7
        else:
            return -1, -1

        return row_i, col_i

    def make_move(self, start_square, end_square):
        """Makes a move on the board, updates game state, checks for winning conditions"""

        if self._game_state == 'WHITE_WON' or self._game_state == 'BLACK_WON':
            return False

        s_row, s_col = self.get_square_i(start_square)
        e_row, e_col = self.get_square_i(end_square)
        if s_row == -1 or e_row == -1:
            if self._debug:
                print(f"Move Error: Squares not valid.")
            return False

        # Start square is holding piece of current turn player
        if self._current_player == 'white' and self._board[s_row][s_col].isupper():
            pass
        elif self._current_player == 'black' and self._board[s_row][s_col].islower():
            pass
        else:
            if self._debug:
                print(f"Move Error: Square was not holding a {self._current_player} piece.")
            return False

        # Check if it is a valid move for that piece
        piece = None
        if self._board[s_row][s_col] == 'P' or self._board[s_row][s_col] == 'p':
            piece = Pawn()

        elif self._board[s_row][s_col] == 'R' or self._board[s_row][s_col] == 'r':
            piece = Rook()

        elif self._board[s_row][s_col] == 'B' or self._board[s_row][s_col] == 'b':
            piece = Bishop()

        elif self._board[s_row][s_col] == 'N' or self._board[s_row][s_col] == 'n':
            piece = Knight()

        elif self._board[s_row][s_col] == 'Q' or self._board[s_row][s_col] == 'q':
            piece = Queen()

        elif self._board[s_row][s_col] == 'K' or self._board[s_row][s_col] == 'k':
            piece = King()
        else:
            exit("Piece unknown")


        eligible_moves = piece.get_moves(s_row, s_col, self._board)

        if (e_row, e_col) not in eligible_moves:
            if self._debug:
                print(f"Move Error: Move not allowed. Allowed: {eligible_moves}")
            return False

        # Checking for winning conditions - king captured
        if self._current_player == 'white' and self._board[e_row][e_col] == "k":
            self._game_state = 'WHITE_WON'

        if self._current_player == 'black' and self._board[e_row][e_col] == "K":
            self._game_state = 'BLACK_WON'

        self._board[e_row][e_col] = self._board[s_row][s_col]
        self._board[s_row][s_col] = " "
        self.switch_player()

        # Checking for winning conditions - king in one of the 4 central squares

        central_squares = [(4,3), (4,4), (3,3), (3,4)]
        if (e_row, e_col) in central_squares:
            if self._board[e_row][e_col] == 'K':
                self._game_state = 'WHITE_WON'
            elif self._board[e_row][e_col] == 'k':
                self._game_state = 'BLACK_WON'

        return True


class Piece:
    """Represents a piece"""
    def __init__(self):
        pass

    def color(self, row, col, board):
        """Returns the color of the piece"""
        if board[row][col].isupper():
            return 'white'
        else:
            return 'black'

    def get_moves(self, row, col, board):
        """Returns the valid move of the piece"""
        return []

    def is_white_piece_at(self, row, col, board):
        """Returns if the white piece is on the square"""
        if board[row][col] != ' ' and board[row][col].isupper():
            return True
        return False

    def is_black_piece_at(self, row, col, board):
        """Returns if the black piece is on the square"""
        if board[row][col] != ' ' and board[row][col].islower():
            return True
        return False

    def is_empty_at(self, row, col, board):
        """Checks if the square is empty"""
        return board[row][col] == ' '

    def is_in_bounds_at(self, row, col):
        """Checks if the move is within the board"""
        if row < 0 or row > 7:
            return False

        if col < 0 or col > 7:
            return False

        return True


class Pawn(Piece):
    """Represents a pawn"""

    def get_moves(self, row, col, board):
        """Returns valid moves of the piece"""
        eligible_moves = []

        if self.color(row, col, board) == 'white':
            max_distance = 1
            if row == 6:
                max_distance = 2

            for i in range(1, 1 + max_distance):
                if self.is_in_bounds_at(row - i, col) and self.is_empty_at(row - i, col, board):
                    eligible_moves.append((row - i, col))
                else:
                    break

            if self.is_in_bounds_at(row - 1, col + 1) and self.is_black_piece_at(row - 1, col + 1, board):
                eligible_moves.append((row - 1, col + 1))

            if self.is_in_bounds_at(row - 1, col - 1) and self.is_black_piece_at(row - 1, col - 1, board):
                eligible_moves.append((row - 1, col - 1))
        else:
            max_distance = 1
            if row == 1:
                max_distance = 2

            for i in range(1, 1 + max_distance):
                if self.is_in_bounds_at(row + i, col) and self.is_empty_at(row + i, col, board):
                    eligible_moves.append((row + i, col))
                else:
                    break

            if self.is_in_bounds_at(row + 1, col + 1) and self.is_white_piece_at(row + 1, col + 1, board):
                eligible_moves.append((row + 1, col + 1))

            if self.is_in_bounds_at(row + 1, col - 1) and self.is_white_piece_at(row + 1, col - 1, board):
                eligible_moves.append((row + 1, col - 1))

        return eligible_moves



class Rook(Piece):
     """Represents a rook"""

     def get_moves(self, row, col, board):
         """Returns valid moves of the rook"""
         eligible_moves = []

         color = self.color(row, col, board)

         max_distance = 7

         for i in range(1, 1 + max_distance):
             if not self.is_in_bounds_at(row - i, col):
                 break
             elif self.is_empty_at(row - i, col, board):
                 eligible_moves.append((row - i, col))
             elif color == 'white' and self.is_black_piece_at(row - i, col, board):
                 eligible_moves.append((row - i, col))
                 break
             elif color == 'black' and self.is_white_piece_at(row - i, col, board):
                 eligible_moves.append((row - i, col))
                 break
             else:
                 break

         for i in range(1, 1 + max_distance):
            if not self.is_in_bounds_at(row + i, col):
                break
            elif self.is_empty_at(row + i, col, board):
                eligible_moves.append((row + i, col))
            elif color == 'white' and self.is_black_piece_at(row + i, col, board):
                eligible_moves.append((row + i, col))
                break
            elif color == 'black' and self.is_white_piece_at(row + i, col, board):
                eligible_moves.append((row + i, col))
                break
            else:
                break

         for i in range(1, 1 + max_distance):
            if not self.is_in_bounds_at(row, col + i):
                break
            elif self.is_empty_at(row, col + i, board):
                eligible_moves.append((row, col + i))
            elif color == 'white' and self.is_black_piece_at(row, col  + i, board):
                eligible_moves.append((row, col  + i))
                break
            elif color == 'black' and self.is_white_piece_at(row, col  + i, board):
                eligible_moves.append((row, col  + i))
                break
            else:
                break

         for i in range(1, 1 + max_distance):
            if not self.is_in_bounds_at(row, col - i):
                break
            elif self.is_empty_at(row, col - i, board):
                eligible_moves.append((row, col - i))
            elif color == 'white' and self.is_black_piece_at(row, col - i, board):
                eligible_moves.append((row, col - i))
                break
            elif color == 'black' and self.is_white_piece_at(row, col - i, board):
                eligible_moves.append((row, col - i))
                break
            else:
                break

         return eligible_moves



class Bishop(Piece):
    """Represents a bishop"""

    def get_moves(self, row, col, board):
        """Returns valid moves of bishop"""
        eligible_moves = []

        color = self.color(row, col, board)

        max_distance = 7

        for i in range(1, 1 + max_distance):
            if not self.is_in_bounds_at(row + i, col + i):
                break
            elif self.is_empty_at(row + i, col + i, board):
                eligible_moves.append((row + i, col + i))
            elif color == 'white' and self.is_black_piece_at(row + i, col + i, board):
                eligible_moves.append((row + i, col + i))
                break
            elif color == 'black' and self.is_white_piece_at(row + i, col + i, board):
                eligible_moves.append((row + i, col + i))
                break
            else:
                break

        for i in range(1, 1 + max_distance):
            if not self.is_in_bounds_at(row - i, col - i):
                break
            elif self.is_empty_at(row - i, col - i, board):
                eligible_moves.append((row - i, col - i))
            elif color == 'white' and self.is_black_piece_at(row - i, col - i, board):
                eligible_moves.append((row - i, col - i))
                break
            elif color == 'black' and self.is_white_piece_at(row - i, col - i, board):
                eligible_moves.append((row - i, col - i))
                break
            else:
                break

        for i in range(1, 1 + max_distance):
            if not self.is_in_bounds_at(row - i, col + i):
                break
            elif self.is_empty_at(row - i, col + i, board):
                eligible_moves.append((row - i, col + i))
            elif color == 'white' and self.is_black_piece_at(row - i, col + i, board):
                eligible_moves.append((row - i, col + i))
                break
            elif color == 'black' and self.is_white_piece_at(row - i, col + i, board):
                eligible_moves.append((row - i, col + i))
                break
            else:
                break

        for i in range(1, 1 + max_distance):
            if not self.is_in_bounds_at(row + i, col - i):
                break
            elif self.is_empty_at(row + i, col - i, board):
                eligible_moves.append((row + i, col - i))
            elif color == 'white' and self.is_black_piece_at(row + i, col - i, board):
                eligible_moves.append((row + i, col - i))
                break
            elif color == 'black' and self.is_white_piece_at(row + i, col - i, board):
                eligible_moves.append((row + i, col - i))
                break
            else:
                break

        return eligible_moves


class Knight(Piece):
    """Represents a knight"""
    def get_moves(self, row, col, board):
        """Returns valid moves of the knight"""

        color = self.color(row, col, board)
        eligible_moves = []
        moves_to_try = [
            (row + 2, col + 1),
            (row + 2, col - 1),
            (row + 1, col + 2),
            (row + 1, col - 2),
            (row - 2, col + 1),
            (row - 2, col - 1),
            (row - 1, col + 2),
            (row - 1, col - 2),
        ]

        for (r, c) in moves_to_try:
            if not self.is_in_bounds_at(r, c):
                continue
            elif self.is_empty_at(r, c, board):
                eligible_moves.append((r, c))
            elif color == 'white' and self.is_black_piece_at(r, c, board):
                eligible_moves.append((r, c))

            elif color == 'black' and self.is_white_piece_at(r, c, board):
                eligible_moves.append((r, c))

        return eligible_moves



class Queen(Piece):
    """Represents a queen"""
    def get_moves(self, row, col, board):
        """Returns valid moves of the queen"""
        eligible_moves = []

        bishop = Bishop()
        rook = Rook()

        for item in (bishop.get_moves(row, col, board)):
            eligible_moves.append(item)
        for item in (rook.get_moves(row, col, board)):
            eligible_moves.append(item)

        return eligible_moves


class King(Piece):
    """Represents a king"""

    def get_moves(self, row, col, board):
        """Returns valid moves of the king"""

        color = self.color(row, col, board)

        eligible_moves = []
        moves_to_try = [
            (row + 1, col),
            (row - 1, col),
            (row + 1, col + 1),
            (row + 1, col - 1),
            (row - 1, col + 1),
            (row - 1, col - 1),
            (row, col + 1),
            (row, col - 1),
        ]

        for (r, c) in moves_to_try:
            if not self.is_in_bounds_at(r, c):
                continue
            elif self.is_empty_at(r, c, board):
                eligible_moves.append((r, c))
            elif color == 'white' and self.is_black_piece_at(r, c, board):
                eligible_moves.append((r, c))

            elif color == 'black' and self.is_white_piece_at(r, c, board):
                eligible_moves.append((r, c))

        return eligible_moves


def test(game, start, end, want_fail=False):
    """Tests the moves implemented"""
    success = game.make_move(start, end)
    if success == want_fail:
        exit(f"Moving {start} to {end} want {not want_fail}, got {success}\n{game.print_board()}")


if __name__ == '__main__':

    # Test a long game with lots of moves from every piece.
    game = ChessVar()
    test(game, "c2","c4")
    test(game, "d7","d6")
    test(game, "d2","d4")
    test(game, "d6","d5")
    test(game, "d4","d5", True)
    test(game, "c4","d5")
    test(game, "a8","a7", True)
    test(game, "a7","a5")
    test(game, "a2","a4")
    test(game, "h7","h5")
    test(game, "a1","a4", True)
    test(game, "a1","a3")
    test(game, "h5","h4")
    test(game, "a3","a2")
    test(game, "h4","h3")
    test(game, "a2","a3")
    test(game, "g7","g6")
    test(game, "a3","b3")
    test(game, "e7","e6")
    test(game, "b3","b2", True)
    test(game, "b3","h3")
    test(game, "h8", "h7")
    test(game, "g2", "g3")
    test(game, "h7", "h3")
    test(game, "c1", "h6")
    test(game, "c8", "e6", True)
    test(game, "f8", "h6")
    test(game, "b1", "c3")
    test(game, "g8", "h6", True)
    test(game, "g8", "f6")
    test(game, "e2", "e4")
    test(game, "f6", "d5")
    test(game, "c3", "b5")
    test(game, "d8", "d6")
    test(game, "d1", "d4", True)
    test(game, "d1", "c2")
    test(game, "d6", "g3")
    test(game, "c2", "d1")
    test(game, "e8", "e7")
    test(game, "e1", "e4", True)
    test(game, "e1", "d2")
    test(game, "e7", "d6")
    test(game, "d2", "d3")
    test(game, "d6", "c5")
    test(game, "d3", "e3")
    test(game, "c5", "b5")
    test(game, "e4", "e5")
    test(game, "b5", "a4")
    test(game, "e3", "e4")
    test(game, "a4", "b4", True)
    # game.print_board()

    # Test a game that ends in a king capture
    game_2 = ChessVar()
    # game_2._debug = True
    test(game_2, "e2", "e4")
    test(game_2, "e7", "e5")
    test(game_2, "e1", "e2")
    test(game_2, "e8", "e7")
    test(game_2, "e2", "e3")
    test(game_2, "e7", "e6")
    test(game_2, "e3", "d3")
    test(game_2, "e6", "d6")
    test(game_2, "d3", "c3")
    test(game_2, "b7", "b5")
    test(game_2, "c3", "c4")
    test(game_2, "b5", "c4")
    test(game_2, "f2", "f3", True) # Game is over

    game_2.print_board()







