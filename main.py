import tkinter # tkinter is the standard GUI library for Python

#game setup
player = "X"
player0 = "O"
curr_player = player
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

color_blue = "#014D66"
color_yellow = "#DADA05"
color_grey = "#808080"
color_light_gray = "#D3D3D3"

#window setup
window = tkinter.Tk()# create the game window
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player+"s turn", font=("consolas", 20), background=color_light_gray,
                      foreground="white")

label.pack()
frame.pack()

window.mainloop()# start the event loop