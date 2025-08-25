def prinyboard():
    print(f"0 | 1 | 2")
    print(f"--|---|---")
    print(f"3 | 4 | 5")
    print(f"--|---|---")
    print(f"6 | 7 | 8")
    pass
    
if __name__ == "__main__":
    xState =[0, 0, 0, 0, 0, 0, 0, 0]
    zState =[0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for X and 0 for O

    print("Welcome to to Tic Tac Toe")
    print("X's chance")
    prinyboard()