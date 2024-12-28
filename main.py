import game_map
import getch

TILE_X = 7
TILE_Y = 11
BOARD_X = 3
BOARD_Y = 3


def process_input(board, key):
    key = key.lower()
    if key == "w" or key == "s" or key == "a" or key == "d":
        board.update_player_pos(key)

def main():
    the_map = game_map.GameMap(BOARD_X, BOARD_Y, TILE_X, TILE_Y)
    the_map.print_curr_tile()
    while True:
        dir = getch.getch()
        process_input(the_map, dir)
        the_map.print_curr_tile()


if __name__ == "__main__":
    main()