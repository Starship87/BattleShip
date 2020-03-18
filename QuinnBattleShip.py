from tkinter import*

root = Tk()
# Tkinter button grids
btn_player_grid = []
btn_opponent_grid = []

frm_player = Frame(root)
frm_opponent = Frame(root)


frm_ships = Frame(root)

WIDTH = 10
HEIGHT = 10
P1_attack = []
P2_attack = []
P1_ships = []
P2_ships = []

P1_shiplist = [
        ["A",2,False],
        ["B",3,False],
        ["C",3,False],
        ["D",4,False],
        ["E",5,False]
    ]
P2_shiplist = [
        ["A",2,False],
        ["B",3,False],
        ["C",3,False],
        ["D",4,False],
        ["E",5,False]
    ]

def fill_board(board):
    temprow = []
    for i in range (WIDTH):
        temprow.append('0')
    for i in range (HEIGHT):
        board.append(temprow.copy())

def show_board(board):
    for i in range (HEIGHT):
        print(board[i])

def create_UI():
    #tkinter code

    #player frame
    lb1=Label(frm_player, text="My Ships", font="Arial 16 bold")
    lb1.grid(row=0, column=0, columnspan=11)

    #column labels
    for i in range(WIDTH):
        lb = Label(frm_player, text=chr(i + 65))
        lb.grid(row=1, column=i+1)

    #row Labels
        for i in range(HEIGHT):
            lb = Label(frm_player, text = i + 1)
            lb.grid(row=i+2, column=0)

            btn_player_grid.append([])
            for j in range(WIDTH):
                btn_player_grid[i].append(Button(frm_player, width=2, height=1))
                btn_player_grid[i][j].row = i
                btn_player_grid[i][j].col = j
                btn_player_grid[i][j].bind("<Button-1>", place_ship)
                
                btn_player_grid[i][j].grid(row=i+2, column=j+1)
         #opponent frame
    lb1=Label(frm_opponent, text="Opponent Ships", font="Arial 16 bold")
    lb1.grid(row=0, column=0, columnspan=11)

    #column labels
    for i in range(WIDTH):
        lb = Label(frm_opponent, text=chr(i + 65))
        lb.grid(row=1, column=i+1)

    #row Labels
        for i in range(HEIGHT):
            lb = Label(frm_opponent, text = i + 1)
            lb.grid(row=i+2, column=0)

            btn_opponent_grid.append([])
            for j in range(WIDTH):
                btn_opponent_grid[i].append(Button(frm_opponent, width=2, height=1))
                btn_opponent_grid[i][j].row = i
                btn_opponent_grid[i][j].col = j
                btn_opponent_grid[i][j].bind("<Button-1>", place_ship)
                
                btn_opponent_grid[i][j].grid(row=i+2, column=j+1)
            
def place_ship(event):
    print(event.widget.row, event.widget.col)
    '''#check first that loacation is valid
    if orient == "hor":
        if col + length > WIDTH:
            print("invalid ship")
            return
        else:
            for i in range (length):
                board[row][col + i] = symbol
                
    if orient == "ver":
        if col + length > HEIGHT:
            print("invalid ship")
            return
        else:
            for i in range (length):
                board[row+i][col] = symbol
                '''
def ship_placement(board):
    for i in range(len(P1_shiplist)):
        print("place ship" + P1_shiplist[i][0]+", length" + str(P1_shiplist[i][1]))
        position = input("Position >>> ")
        orient = input("Orientation >>> ")
        col = ord (position[0].upper()) - 65
        row = int (position[1:]) -1
        
        place_ship(P1_shiplist[i][0],P1_shiplist[i][1], row, col,orient,board)
        
        
    
def start_game():
    fill_board(P1_attack)
    fill_board(P2_attack)
    fill_board(P1_ships)
    fill_board(P2_ships)
create_UI()

frm_player.grid(row=0, column=0)
frm_opponent.grid(row=0, column=1)
frm_ships.grid(row=1, column=0, columnspan=2)
root.mainloop()
