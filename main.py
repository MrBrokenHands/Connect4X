#Grid
grid = [["-" * 7] * 6]

#Menu
def menu(): 
    menu = "Connect 4 - Press the enter key to play"
    print(menu)
    input()

def move():
    while True:
        column = input("Pick a Column (1-7)")
        column = int(column)
        if column >= 1 and <= 7:
            continue
        else:
            break
    if grid

    
menu()

#James Worley and Tom Comrie 09/09/2020