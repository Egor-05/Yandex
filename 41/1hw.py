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
    def __init__(self, color):
        super().__init__(color)
        self.moved = False

    def char(self):
        return 'K'

    def can_move(self, field, y1, x1, row, col):
        if abs(x1 - col) <= 1 and abs(y1 - row) <= 1:
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
        if y1 == start_row and y1 + 2 * direction == row and col == x1:
            super().can_move(field, y1, x1, row, col)
            return True

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
    def __init__(self, color):
        super().__init__(color)
        self.moved = False

    def char(self):
        return 'R'

    def can_move(self, field, y1, x1, row, col):
        if y1 != row and x1 != col:
            super().can_move(field, y1, x1, row, col)
            return False
        return True


class Bishop(Figure):
    def char(self):
        return 'B'

    def can_move(self, field, y1, x1, row, col):
        if abs(y1 - row) == abs(x1 - col):
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
        if self.field[row][col].char() in ['R', 'K']:
            self.field[row][col].moved = True
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
                        if piece.can_move(self, i, j, row, col):
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
            self.color = opponent(self.color)
            return True
        return False

    def space(self, line, start, end):
        for i in range(start + 1, end):
            if self.field[line][i] is not None:
                return False
        return True

    def castling(self, col):
        row = 0 if self.color == WHITE else 7
        cur_row = self.field[row]
        a = self.space(row, min(col, 4), max(col, 4))
        if (cur_row[col] is not None and cur_row[col].char() == 'R' and not cur_row[col].moved) and \
           (cur_row[4] is not None and cur_row[4].char() == 'K' and not cur_row[4].moved) and a:
            cur_row[col] = cur_row[4] = None
            if col == 0:
                cur_row[3] = Rook(self.color)
                cur_row[2] = King(self.color)
            else:
                cur_row[5] = Rook(self.color)
                cur_row[6] = King(self.color)
            self.color = opponent(self.color)
            return True
        return False

    def castling0(self):
        return self.castling(0)

    def castling7(self):
        return self.castling(7)



board = Board()
board.field = [([None] * 8) for i in range(8)]
board.field[0][0] = Knight(WHITE)
board.field[0][4] = King(WHITE)
board.field[0][7] = Bishop(WHITE)

board.field[7][0] = Queen(BLACK)
board.field[7][4] = King(BLACK)
board.field[7][7] = Pawn(BLACK)

board.field[1][4] = Pawn(WHITE)

print('before:')
for row in range(7, -1, -1):
    for col in range(8):
        char = board.cell(row, col)[1]
        print(char.replace(' ', '-'), end='')
    print()
print()

print("Попытки рокировок короля не с ладьёй")
print(board.castling0())
print(board.castling7())

print('3 turns after:')
for row in range(7, -1, -1):
    for col in range(8):
        char = board.cell(row, col)[1]
        print(char.replace(' ', '-'), end='')
    print()
print()

board.move_piece(1, 4, 3, 4)
print(board.castling0())
print(board.castling7())
