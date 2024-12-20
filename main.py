import time
import board
import getch

BOARD_X = 7
BOARD_Y = 11

def main():
    play_map = board.Board(BOARD_X, BOARD_Y)
    time.sleep(0.5)
    play_map.print_board()
    while True:
        dir = getch.getch()
        play_map.update_player_pos(dir)
        play_map.print_board()


if __name__ == "__main__":
    main()