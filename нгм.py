WHITE = 1
BLACK = 2


def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE


def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


class Figure:
    def __init__(self, color):
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def get_color(self):
        return self.color

    def can_move(self, field, y1, x1, row, col):
        if row == y1 and col == x1 or field.field[row][col] is not None:
            return False
        dx = x1 - col
        dy = y1 - row
        for i in range(max(abs(dx), abs(dy))):
            x = x1 + 1 * (-(abs(dx) // dx) if dx != 0 else 0)
            y = y1 + 1 * (-(abs(dy) // dy) if dy != 0 else 0)
            if field.field[y][x] is not None:
                return False
        return True


class King(Figure):
    def char(self):
        return 'K'

    def can_move(self, field, y1, x1, row, col):
        if abs(x1 - row) <= 1 and abs(y1 - row) <= 1:
            super().can_move(field, x1, y1, row, col)
            return True
        return False


class Queen(Figure):
    def char(self):
        return 'Q'

    def can_move(self, field, y1, x1, row, col):
        if (abs(y1 - row) == abs(x1 - col)) or \
                (abs(y1 - row) * abs(x1 - col) == 0):
            return super().can_move(field, y1, x1, row, col)
        return False


class Knight(Figure):
    def char(self):
        return 'N'

    def can_move(self, field, y1, x1, row, col):
        if abs(self.col - col) * abs(self.row - row) == 2 and \
                self.row != row and self.col != col:
            return True
        return False


class Pawn(Figure):
    def char(self):
        return 'P'

    def can_move(self, field, y1, x1, row, col):
        if self.col != col:
            return False
        if self.color == WHITE:
            direction = -1
            start_row = 6
        else:
            direction = 1
            start_row = 1
        if self.row + direction == row:
            super().can_move(field, y1, x1, row, col)
            return True
        if self.row == start_row and self.row + 2 * direction == row:
            super().can_move(field, y1, x1, row, col)
            return True
        return False


class Rook(Figure):
    def char(self):
        return 'R'

    def can_move(self, field, y1, x1, row, col):
        if self.row != row and self.col != col:
            super().can_move(field, y1, x1, row, col)
            return False
        return True


class Bishop(Figure):
    def char(self):
        return 'B'

    def can_move(self, field, y1, x1, row, col):
        if abs(self.row - row) == abs(self.col - col):
            super().can_move(field, y1, x1, row, col)
            return True
        return False


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = [[Rook(BLACK), Knight(BLACK),
                       Bishop(BLACK), Queen(BLACK),
                       King(BLACK), Bishop(BLACK),
                       Knight(BLACK), Rook(BLACK)],
                      [Pawn(BLACK), Pawn(BLACK),
                       Pawn(BLACK), Pawn(BLACK),
                       Pawn(BLACK), Pawn(BLACK),
                       Pawn(BLACK), Pawn(BLACK)],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [None, None, None, None, None, None, None, None],
                      [Pawn(WHITE), Pawn(WHITE),
                       Pawn(WHITE), Pawn(WHITE),
                       Pawn(WHITE), Pawn(WHITE),
                       Pawn(WHITE), Pawn(WHITE)],
                      [Rook(WHITE), Knight(WHITE),
                       Bishop(WHITE), Queen(WHITE),
                       King(WHITE), Bishop(WHITE),
                       Knight(WHITE), Rook(WHITE)]]

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        piece = self.field[row][col]
        if piece is None:
            return '  '
        return ' ' + piece.char()

    def move_piece(self, row, col, row1, col1):
        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.current_player_color():
            return False
        if not piece.can_move(self.field, row, col, row1, col1):
            return False
        if isinstance(piece, King) and self.is_under_attack(row1, col1, opponent(self.color)):
            return False
        self.field[row][col] = None
        self.field[row1][col1] = piece
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True

    def is_under_attack(self, row, col, color):
        for i in range(8):
            for j in range(8):
                if self.field[i][j] is not None:
                    piece = self.field[i][j]
                    if piece.get_color() == color:
                        if piece.can_move(self.field, j, i, row, col):
                            return True
        return False

    def get_piece(self, y, x):
        return self.field[y][x]


board = Board()
board.field = [([None] * 8) for i in range(8)]
board.field[0][3] = Queen(WHITE)
queen = board.get_piece(0, 3)

for row in range(7, -1, -1):
    for col in range(8):
        if queen.can_move(board, 0, 3, row, col):
            print('x', end='')
        else:
            cell = board.cell(row, col)[1]
            cell = cell if cell != ' ' else '-'
            print(cell, end='')
    print()


board = Board()
board.field = [([None] * 8) for i in range(8)]
board.field[0][3] = Queen(WHITE)
board.field[2][3] = Bishop(WHITE)
board.field[0][5] = Rook(WHITE)
queen = board.get_piece(0, 3)

for row in range(7, -1, -1):
    for col in range(8):
        if queen.can_move(board, 0, 3, row, col):
            print('x', end='')
        else:
            cell = board.cell(row, col)[1]
            cell = cell if cell != ' ' else '-'
            print(cell, end='')
    print()


board = Board()
board.field = [([None] * 8) for i in range(8)]
queen = Queen(BLACK)
r0, c0 = 4, 5
board.field[r0][c0] = queen
board.field[4][2] = Pawn(BLACK)
board.field[6][5] = Pawn(WHITE)

for row in range(7, -1, -1):
    for col in range(8):
        if queen.can_move(board, r0, c0, row, col):
            print('x', end='')
        else:
            cell = board.cell(row, col)[1]
            cell = cell if cell != ' ' else '-'
            print(cell, end='')
    print()