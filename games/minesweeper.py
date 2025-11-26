'''
simple Minesweeper game code for learning how does it work
'''
import random

def creat_board(size=5, mines=5):
    board = [[" " for _ in range(size)] for _ in range(size)]
    mine_positions = set()
    while len(mine_positions) < mines:
        mine_positions.add((
        random.randint(0, size -1),
        random.randint(0, size -1)))
    #for test only
    print("mine position=", mine_positions)
    return board, mine_positions
    
def neighbors_count(r, c, mine_positions, size):
    neighbors = [ 
    (r-1,c-1), (r-1,c), (r-1,c+1),
    (r,c-1),            (r,c+1),
    (r+1,c-1), (r+1,c), (r+1,c+1)
    ]
    count = 0
    
    for nr , nc in neighbors:
        if 0 <= nr < size and 0 <= nc < size:
            if (nr,nc) in mine_positions:
                count += 1
            
    return count

def print_board(board):
    print("\n  " + " ".join(str(i) for i in range(len(board))))
    print("  " + "--" * len(board))
    for i, row in enumerate(board):
        print(i, "|", " ".join(row))
        
    
def open_cell(r, c, board, mine_positions, size):
    if (r, c) in mine_positions:
        board[r][c] = "💣"
        print_board(board)
        print("\n💥 BOOM! You hit a mine. Game over.")
        return False
    
    count = neighbors_count(r, c, mine_positions, size)
    board [r][c] = str(count)
    
    return True

size = 5
mines = 5
board, mine_position = creat_board(size)
print("The bombs were planted")

while True:
    print_board(board)
    
    try:
        user_command = input("Enter your choice(open row col): ").split()
        if user_command[0] != "open":
            print("use command : (open row col)")
            continue
        
        r = int(user_command[1])
        c = int(user_command[2])
        
    except:
        print("invalid input..use command example: open 1 2")
        continue
    if not (0 <= r < size and 0 <= c < size):
        print("out of range")
        continue
    
    result = open_cell(r, c, board, mine_position, size)
    if not result:
        break