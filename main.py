import time
import board
import getch

BOARD_X = 7
BOARD_Y = 11


def process_input(board, key):
    key = key.lower()
    if key == "w" or key == "s" or key == "a" or key == "d":
        board.update_player_pos(key)

def main():
    play_map = board.Board(BOARD_X, BOARD_Y)
    time.sleep(0.5)
    play_map.print_board()
    while True:
        dir = getch.getch()
        process_input(play_map, dir)
        play_map.print_board()


if __name__ == "__main__":
    main()