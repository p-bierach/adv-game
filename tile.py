import os
import random

decorations = ['.','1','^','@','T','=']

class Tile:
    layout = [[]]
    last_space = "*"
    player_r = 0
    player_c = 0
    tile_r = 0
    tile_c = 0

    def __init__(self, x, y, starting):
        self.tile_r = x
        self.tile_c = y
        self.layout = [[0] * y for i in range(x)]
        self.player_r = int(len(self.layout) / 2)
        self.player_c = int(len(self.layout[0])/2)
        self.gen_tile(starting)

    def gen_tile(self, starting):
        for r in range(len(self.layout)):
            for c in range(len(self.layout[0])):
                if starting and r == int(self.tile_r/2):
                    self.layout[r][c] = "-"
                elif starting and c == int(self.tile_c/2):
                    self.layout[r][c] = "|"
                else:
                    self.layout[r][c] = "*"

        if(starting):
            self.layout[int(self.tile_r/2)][int(self.tile_c/2)] = "X"
            self.last_space = "0"
        else:
            rand = random.randint(0,1)
            if rand == 0:
                self.__decorate()


    def print_tile(self):
        os.system("clear")
        row_as_str = ""
        for r in range(len(self.layout)):
            for c in range(len(self.layout[0])):
                row_as_str += self.layout[r][c]
            print(row_as_str)
            row_as_str = ""

#decorations = ['.','1','^','@','+','=']

    def __decorate(self):
        dec_index = random.randint(0, len(decorations)-1)
        if dec_index == 0: #'.' square
            corner = random.randint(1, 3)
            col = random.randint(2, 6)
            for i in range(3):
                self.layout[corner][col+i] = '.'

            self.layout[corner+1][col] = '.'
            self.layout[corner+1][col+2] = '.'

            for i in range(3):
                self.layout[corner+2][col+i] = '.'
        elif dec_index == 1: #field of ones
            for r in range(len(self.layout)):
                for c in range(len(self.layout[0])):
                    self.layout[r][c] = '1'
        elif dec_index == 2: #'^' row
            row = random.randint(1, 3)
            col = random.randint(2, 4)
            for i in range(5):
                if i % 2 == 1:
                    continue
                for j in range(5):
                    self.layout[row+i][col+j] = '^'
        else: #spread about
            for i in range(10):
                row = random.randint(0, 6)
                col = random.randint(0, 10)
                self.layout[row][col] = decorations[dec_index]