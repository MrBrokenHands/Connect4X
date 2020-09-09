#Grid
grid = [["-" * 7] * 6]

#Menu
def menu(): 
    print("Connect 4 - Press the enter key to play")
    input()
    currentPlayer = str(input("Red or Yellow?")) #Either set as "Y" or "R"

def move():
  valid = False
  while True:
    while valid == False:
      try:
        column = ""
        column = int(input("Pick a Column (1-7)"))
        valid = True
      except:
          print("Please enter a number")
      try:
        if column >= 1 and column <= 7:
          break
        else:
          print("Input is not valid number")
          valid = False
          continue
      except:
        print("Input is not valid number")
    break
  return(column)

def checkMove(column):
    for x in range(6):
      print(x)
      if grid[x, column] != "-":
          grid[x, column] = 

#menu()
column=move()
checkMove(column)
print("END OF PROGRAM")

#James Worley and Tom Comrie 09/09/2020