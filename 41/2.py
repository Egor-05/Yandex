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
        if row == y1 and col == x1:
            return False
        dx = x1 - col
        dy = y1 - row
        x = x1
        y = y1
        for i in range(max(abs(dx), abs(dy))):
            x += 1 * (-(abs(dx) // dx) if dx != 0 else 0)
            y += 1 * (-(abs(dy) // dy) if dy != 0 else 0)
            if field.field[y][x] is not None:
                if x == col and y == row and \
                        field.field[y][x].get_color() != field.field[y1][x1].get_color():
                    return True
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
        if abs(x1 - col) * abs(y1 - row) == 2 and \
                x1 != row and x1 != col:
            return True
        return False


class Pawn(Figure):
    def char(self):
        return 'P'

    def can_move(self, field, y1, x1, row, col):
        if field.field[y1][x1].get_color() == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6
        if y1 + direction == row and col == x1 and field.field[row][col] is None:
            super().can_move(field, y1, x1, row, col)
            return True

        b = field.field[y1 + direction]
        if y1 + direction == row:
            if x1 + 1 == col and b[x1 + 1] is not None and \
                    b[x1 + 1].get_color() != field.field[y1][x1].get_color() or \
                    x1 - 1 == col and b[x1 - 1] is not None and \
                    b[x1 - 1].get_color() != field.field[y1][x1].get_color():
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
        if not piece.can_move(self, row, col, row1, col1):
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
                        if piece.can_move(self, j, i, row, col):
                            return True
        return False

    def get_piece(self, y, x):
        return self.field[y][x]

    def move_and_promote_pawn(self, row, col, row1, col1, char):
        if self.field[row][col] is not None and \
                self.field[row][col].char() == 'P' and \
                self.field[row][col].can_move(self, row, col, row1, col1):
            b = None
            c = self.field[row][col].get_color()
            if char == 'Q':
                b = Queen(c)
            elif char == 'R':
                b = Rook(c)
            elif char == 'B':
                b = Bishop(c)
            elif char == 'N':
                b = Knight(c)
            self.field[row][col] = None
            self.field[row1][col1] = b
            return True
        else:
            return False


board = Board()
board.field = [([None] * 8) for i in range(8)]
board.field[6][0] = Pawn(WHITE)
board.field[6][1] = Pawn(WHITE)
board.field[6][7] = Pawn(WHITE)

board.field[2][1] = Pawn(BLACK)
board.field[2][4] = Pawn(BLACK)

print('before:')
for row in range(7, -1, -1):
    for col in range(8):
        char = board.cell(row, col)[1]
        print(char.replace(' ', '-'), end='')
    print()
print()


print(board.move_and_promote_pawn(6, 0, 7, 0, 'Q'))
print(board.move_piece(2, 1, 1, 1))

print(board.move_and_promote_pawn(6, 1, 7, 1, 'N'))
print(board.move_piece(2, 4, 1, 4))

print(board.move_piece(7, 1, 6, 3))
print(board.move_and_promote_pawn(1, 1, 0, 1, 'R'))

print(board.move_piece(6, 3, 7, 5))
print(board.move_and_promote_pawn(1, 4, 0, 4, 'Q'))

print(board.move_and_promote_pawn(6, 7, 7, 7, 'Q'))

print(board.get_piece(7, 0).get_color())
print(board.get_piece(7, 5).get_color())
