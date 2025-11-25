'''
simple Minesweeper game code for learning how does it work
'''
import random

def creat_board(size=5, mines=5):
    board = [[" " for i in range(size)] for _ in range(size)]
    mine_positions = set()
    while len(mine_positions) < mines:
        mine_positions.add((
        random.randint(0, size -1),
        random.randint(0, size -1)))
    
    print("mine position=", mine_positions)
    return board, mine_positions
    
