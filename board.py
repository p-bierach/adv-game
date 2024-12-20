import os
import time


class Board:
    board = [[]]
    player_r = 0
    player_c = 0
    board_r = 0
    board_c = 0

    def __init__(self, x, y):
        self.board_r = x
        self.board_c = y
        self.board = [[0] * y for i in range(x)]
        self.player_r = int(len(self.board) / 2)
        self.player_c = int(len(self.board[0])/2)
        self.gen_board()
        self.board[self.player_r][self.player_c] = "X"

    def gen_board(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                self.board[r][c] = "*"

    def print_board(self):
        os.system("clear")
        row_as_str = ""
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                row_as_str += self.board[r][c]
            print(row_as_str)
            row_as_str = ""

    def update_player_pos(self, dir):
        old_r = self.player_r
        old_c = self.player_c
        same_board = False #if false, gen a new board
        keep_rows = False #used in conjunction with same_board to determine player pos on new board
        keep_cols = False

        dir = dir.lower()
        if dir == "w":
            if not self.out_of_bounds(True, self.player_r-1):
                self.player_r -= 1
                same_board = True
            else:
                keep_cols = True
        elif dir == "s":
            if not self.out_of_bounds(True, self.player_r+1):
                self.player_r += 1
                same_board = True
            else:
                keep_cols = True
        elif dir == "a":
            if not self.out_of_bounds(False, self.player_c-1):
                self.player_c -= 1
                same_board = True
            else:
                keep_rows = True
        elif dir == "d":
            if not self.out_of_bounds(False, self.player_c+1):
                self.player_c += 1
                same_board = True
            else:
                keep_rows = True

        if same_board:
            self.board[old_r][old_c] = "*"
            self.board[self.player_r][self.player_c] = "X"
        else:
            #update player coords
            if keep_rows:
                #self.player_r = 0
                self.player_c = 0 if self.player_c == self.board_c - 1 else self.board_c - 1
            if keep_cols:
                #self.player_c = 0
                self.player_r = 0 if self.player_r == self.board_r - 1 else self.board_r - 1
            #gen new board and update player pos
            self.gen_board()
            self.board[self.player_r][self.player_c] = "X"




    def out_of_bounds(self, row, pos):
        if row:
            if(pos < 0 or pos > len(self.board)-1):
                return True
        else:
            if (pos < 0 or pos > len(self.board[0])-1):
                return True
        return False





