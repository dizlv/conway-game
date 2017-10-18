import random

import board
import cell

BOARD_WIDTH = 4
BOARD_HEIGHT = 4

states = list(cell.CellState)


def make_game_board():
    game_board = board.Board(BOARD_WIDTH, BOARD_HEIGHT)

    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            game_board._board[x][y] = cell.Cell(x, y, random.choice(states))

    return game_board


if __name__ == '__main__':
    game_board = make_game_board()

    for i in range(10):
        game_board.new_generation()

        print(game_board)
