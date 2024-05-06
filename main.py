import time

from View.board import *
from GameLogic.alphaBetaPruning import *
import math


def main():
    grid = [
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, 1, 0, -1, -1, -1],
        [-1, -1, -1, 0, 1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
    ]

    color = 0
    count = 1
    while True:
        print("0 score:  " + str(evaluate(grid, 0)))
        print("1 score:  " + str(evaluate(grid, 1)))
        print(color)
        print("#"+str(count))
        bestMove = get_best_move(grid, color, 10)
        for j in grid:
            print(j)
        if bestMove[0] == -1:
            break
        grid = update_board(grid, bestMove[0], bestMove[1], color)
        for j in grid:
            print(j)
        print('------------------------------------------------------------------------------------------------------------------------')
        color = 1 - color
        count += 1
        # time.sleep(4)
    # root = tk.Tk()
    # board = Board(root)
    # root.mainloop()


if __name__ == "__main__":
    main()
