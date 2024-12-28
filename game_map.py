import tile
import os

class GameMap:
    board_r = 0 #refers to number of tiles on map
    board_c = 0
    tile_r = 0 #refers to size of tile
    tile_c = 0

    curr_r = 0 #refers to player's current tile
    curr_c = 0
    board = [[]]
    curr_tile = None

    def __init__(self, r, c, tile_r, tile_c):
        self.board_r = r
        self.board_c = c
        self.board = [[0] * c for i in range(r)]
        self.tile_r = tile_r
        self.tile_c = tile_c
        self.__gen_map()
        self.curr_tile = self.board[int(r/2)][int(c/2)]
        self.curr_r = int(r/2)
        self.curr_c = int(c/2)

    def __gen_map(self):
        i = 1
        for r in range(0, self.board_r):
            for c in range(0, self.board_c):
                curr = tile.Tile(self.tile_r, self.tile_c)
                curr.layout[0][0] = str(i)
                i+=1
                self.board[r][c] = curr
                if r == int(self.board_r/2) and c == int(self.board_c/2): #middle tile
                    curr.last_space = "0"

    def print_curr_tile(self):
        self.curr_tile.print_tile()

    def update_player_pos(self, dir):
        old_r = self.curr_tile.player_r
        old_c = self.curr_tile.player_c
        same_tile = False  # if false, gen a new tile

        if dir == "w":
            if not self.__tile_out_of_bounds(True, self.curr_tile.player_r - 1):
                self.curr_tile.player_r -= 1
                same_tile = True
        elif dir == "s":
            if not self.__tile_out_of_bounds(True, self.curr_tile.player_r + 1):
                self.curr_tile.player_r += 1
                same_tile = True
        elif dir == "a":
            if not self.__tile_out_of_bounds(False, self.curr_tile.player_c - 1):
                self.curr_tile.player_c -= 1
                same_tile = True
        elif dir == "d":
            if not self.__tile_out_of_bounds(False, self.curr_tile.player_c + 1):
                self.curr_tile.player_c += 1
                same_tile = True

        if same_tile:
            self.curr_tile.layout[old_r][old_c] = self.curr_tile.last_space
            self.curr_tile.last_space = self.curr_tile.layout[self.curr_tile.player_r][self.curr_tile.player_c]
            self.curr_tile.layout[self.curr_tile.player_r][self.curr_tile.player_c] = "X"
        else:
            self.curr_tile.layout[self.curr_tile.player_r][self.curr_tile.player_c] = self.curr_tile.last_space
            if not self.__update_to_new_tile(dir):
                self.curr_tile.layout[self.curr_tile.player_r][self.curr_tile.player_c] = "X"


    def __tile_out_of_bounds(self, row, pos):
        if row:
            if pos < 0 or pos > self.tile_r - 1:
                return True
        else:
            if pos < 0 or pos > self.tile_c - 1:
                return True
        return False

    def __update_to_new_tile(self, dir):
        if dir == "w": #up
            if not self.__board_out_of_bounds(True, self.curr_r - 1):
                self.__set_cur_tile(self.curr_r - 1, self.curr_c, False)
                return True
        if dir == "s": #down
            if not self.__board_out_of_bounds(True, self.curr_r + 1):
                self.__set_cur_tile(self.curr_r + 1, self.curr_c, False)
                return True
        if dir == "a": #left
            if not self.__board_out_of_bounds(False, self.curr_c - 1):
                self.__set_cur_tile(self.curr_r, self.curr_c - 1, True)
                return True
        if dir == "d": #right
            if not self.__board_out_of_bounds(False, self.curr_c + 1):
                self.__set_cur_tile(self.curr_r, self.curr_c + 1, True)
                return True

        return False

    def __board_out_of_bounds(self, row, pos):
        if row:
            if pos < 0 or pos > self.board_r - 1:
                return True
        else:
            if pos < 0 or pos > self.board_c - 1:
                return True
        return False

    def __set_cur_tile(self, r, c, keep_row):
        old_player_r = self.curr_tile.player_r
        old_player_c = self.curr_tile.player_c

        #update tile coords for map
        self.curr_tile = self.board[r][c]
        self.curr_r = r
        self.curr_c = c
        #update player coords for tile
        if keep_row:
            self.curr_tile.player_c = 0 if old_player_c == self.tile_c-1 else self.tile_c-1
            self.curr_tile.player_r = old_player_r
        else:
            self.curr_tile.player_r = 0 if old_player_r == self.tile_r-1 else self.tile_r-1
            self.curr_tile.player_c = old_player_c

        self.curr_tile.layout[self.curr_tile.player_r][self.curr_tile.player_c] = "X"
