class Analysis:

    def __init__(self, board: list[int] = [0] * 9):
        self.board: list[int] = board

    def winner(self):
        vertical_left = self.board[0] == self.board[3] == self.board[6] and self.board[0] != 0
        vertical_middle = self.board[1] == self.board[4] == self.board[7] and self.board[1] != 0
        vertical_right = self.board[2] == self.board[5] == self.board[8] and self.board[2] != 0
        horizontal_top = self.board[0] == self.board[1] == self.board[2] and self.board[0] != 0
        horizontal_middle = self.board[3] == self.board[4] == self.board[5] and self.board[3] != 0
        horizontal_bottom = self.board[6] == self.board[7] == self.board[8] and self.board[6] != 0
        diagonal_topleft_bottomright = self.board[0] == self.board[4] == self.board[8] and self.board[0] != 0
        diagonal_topright_bottomleft = self.board[2] == self.board[4] == self.board[6] and self.board[2] != 0
        if (
            vertical_left
            or vertical_middle
            or vertical_right
            or horizontal_top
            or horizontal_middle
            or horizontal_bottom
            or diagonal_topleft_bottomright
            or diagonal_topright_bottomleft
        ):
            if vertical_middle or horizontal_middle or diagonal_topleft_bottomright or diagonal_topright_bottomleft:
                return self.board[4]
            elif vertical_left or horizontal_top:
                return self.board[0]
            elif vertical_right or horizontal_bottom:
                return self.board[8]
        return 0
