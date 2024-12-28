import os

class Tile:
    layout = [[]]
    last_space = "*"
    player_r = 0
    player_c = 0
    tile_r = 0
    tile_c = 0

    def __init__(self, x, y):
        self.tile_r = x
        self.tile_c = y
        self.layout = [[0] * y for i in range(x)]
        self.player_r = int(len(self.layout) / 2)
        self.player_c = int(len(self.layout[0])/2)
        self.gen_tile()

    def gen_tile(self):
        #add a path
        #if not path make *
        for r in range(len(self.layout)):
            for c in range(len(self.layout[0])):
                self.layout[r][c] = "*"

    def print_tile(self):
        os.system("clear")
        row_as_str = ""
        for r in range(len(self.layout)):
            for c in range(len(self.layout[0])):
                row_as_str += self.layout[r][c]
            print(row_as_str)
            row_as_str = ""