#Grid
grid = [["-" * 7] * 6]

#Menu
def menu(): 
    menu = "Connect 4 - Press the enter key to play"
    print(menu)
    input()

def move():
    while True:
      while True:
        try:
          column = ""
          column = int(input("Pick a Column (1-7)"))
          break
        except:
          print("Please enter a number retard")
        try:
          if column >= 1 and column <= 7:
            print("Yes")
            break
          else:
            print("Input is not valid")
            continue
        except:
            print("not valid input")
    #if grid

    
menu()
move()
#James Worley and Tom Comrie 09/09/2020