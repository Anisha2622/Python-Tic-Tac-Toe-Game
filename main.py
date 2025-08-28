import tkinter # tkinter is the standard GUI library for Python

def set_title(row, column):
    global curr_player

    if game_over: # check if the game is over
        return

    if board[row][column]["text"] != "": 
        # alraedy taken spot
        return

    board[row][column]["text"] = curr_player # mark the board

    if curr_player == playerO: # switch players
        curr_player = playerX
    else:
        curr_player = playerO

    label["text"] = curr_player + "s turn" # update the label

# check winner
    check_winner()

def check_winner():
    global turns, game_over
    turns += 1

    # horizonttally check 3 rows
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
            and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"] + " is the winner!", foreground=color_yellow)
            for column in range(3):
                board[row][column].config(background=color_light_gray)
            game_over = True
            return

# vertically check 3 columns
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
            and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"] + " is the winner!", foreground=color_yellow)
            for row in range(3):
                board[row][column].config(background=color_light_gray)
            game_over = True
            return
        
# diagonally check 
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
        and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"] + " is the winner!", foreground=color_yellow)
        for i in range(3):
            board[i][i].config(background=color_light_gray)
        game_over = True
        return

#anti-diagonally check
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
        and board[0][2]["text"] != ""):
        label.config(text=board[0][0]["text"] + " is the winner!", foreground=color_yellow)
        board[0][2].config(foreground=color_yellow, background=color_light_gray)
        board[1][1].config(foreground=color_yellow, background=color_light_gray)
        board[2][0].config(foreground=color_yellow, background=color_light_gray)
        game_over = True
        return
    
# check for tie
    if turns == 9:
        game_over = True
        label.config(text="It's a tie!", foreground=color_yellow)
        
def new_game():
    global turns, game_over

    turns = 0
    game_over = False
    label["text"] = curr_player + "s turn"

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", background=color_gray, foreground=color_blue)
#game setup
playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

color_blue = "#014D66"
color_yellow = "#DADA05"
color_gray = "#272525"
color_light_gray = "#D3D3D3"

turns = 0
game_over = False

#window setup
window = tkinter.Tk()# create the game window
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player+"s turn", font=("consolas", 20), background=color_light_gray,
                      foreground="white")

label.grid(row=0, column=0,columnspan=3, sticky= "we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("consolas", 50, "bold"), 
                                        background=color_gray, foreground=color_blue, width=4, height=1,
                                        command=lambda row=row, column= column: set_title(row, column))
        board[row][column].grid(row=row+1, column=column)
       
button = tkinter.Button(frame, text="Restart", font=("consolas", 20), background=color_gray,
                        foreground="white", command=new_game)

button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()

# center the window on the screen
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

# format "(width)x(height)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


window.mainloop()# start the event loop