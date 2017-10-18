import cell
import utils

import numpy as np


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self._board = utils.generate_matrix(self.width, self.height)
        self._next_board = utils.generate_matrix(self.width, self.height)

    @property
    def board(self):
        return self._board

    def get_cell_state(self, x, y):
        return self._board[x][y].state

    def count_neighbours(self, x, y):
        count = 0

        for offset in cell.Offset:
            new_x = x + offset.value.delta_x
            new_y = y + offset.value.delta_y

            if (new_x <= self.width - 1) and (new_y <= self.height - 1):
                cell_state = self.get_cell_state(new_x, new_y)

                if cell_state == cell.CellState.LIVE:
                    count += 1

        return count

    def get_new_cell_state(self, x, y, neighbours):
        cell_state = self.get_cell_state(x, y)

        if cell_state == cell.CellState.LIVE:
            if neighbours <= 2:
                return cell.CellState.DEAD

            elif 3 <= neighbours >= 2:
                return cell.CellState.LIVE

            elif neighbours > 3:
                return cell.CellState.DEAD

        else:
            if neighbours == 3:
                return cell.CellState.LIVE

            else:
                return cell.CellState.DEAD

    def calculate(self):
        width_range = range(self.width)
        height_range = range(self.height)

        for x in width_range:
            for y in height_range:
                neighbours = self.count_neighbours(x, y)

                state = self.get_new_cell_state(x, y, neighbours)

                self._next_board[x][y] = cell.Cell(x, y, state)

    def new_generation(self):
        self.calculate()
        self._board = self._next_board

    def __str__(self):
        return str(np.matrix(self.board))
