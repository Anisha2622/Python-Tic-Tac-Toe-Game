import tkinter # tkinter is the standard GUI library for Python

def set_title(row, column):
    pass
#game setup
player = "X"
player0 = "O"
curr_player = player
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

color_blue = "#014D66"
color_yellow = "#DADA05"
color_gray = "#808080"
color_light_gray = "#D3D3D3"

#window setup
window = tkinter.Tk()# create the game window
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player+"s turn", font=("consolas", 20), background=color_light_gray,
                      foreground="white")

label.grid(row=0, column=0)

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("consolas", 50, "bold"), 
                                        background=color_gray, foreground=color_blue, width=4, height=1,
                                        command=lambda row=row, column= column: set_title(row, column))
        board[row][column].grid(row=row+1, column=column)
       

frame.pack()

window.mainloop()# start the event loop