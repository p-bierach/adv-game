import os

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


    def print_tile(self):
        os.system("clear")
        row_as_str = ""
        for r in range(len(self.layout)):
            for c in range(len(self.layout[0])):
                row_as_str += self.layout[r][c]
            print(row_as_str)
            row_as_str = ""