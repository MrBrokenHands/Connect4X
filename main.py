#global check
#Grid
grid = [["-" * 7] * 6]
def displayGrid():
    print(grid)

#ValidityChecker
def validCheck(dataType):
  dataType = str(dataType)
  valid = False
  while True:
    while valid == False:
      if dataType == "number":
        try:
          check = ""
          check = int(input("Pick a Column (1-7)\n"))
          print()
          valid = True
        except:
          print("Input is not a valid",dataType)
      elif dataType == "colour":
        try:
          check = ""
          check = str(input("Pick a Colour (R or Y)\n"))
          print()
          valid = True
        except:
            print("Please enter a colour (R or Y)\n")
      if dataType == "colour":
        try:
          if check == "R" or check == "Y":
            break
          else:
            print("Input is not a valid",dataType)
            valid = False
            continue
        except:
          print("Input is not a valid",dataType)
      elif dataType == "number":
        try:
          if check >= 1 and check <= 7:
            break
          else:
            print("Input is not a valid",dataType)
            valid = False
            continue
        except:
          continue
    break
  return(check)
  
#Menu
def menu(): 
    print("The Lad's Connect 4 - Press the enter key to play")
    input()
    dataType = "colour"
    currentPlayer = validCheck(dataType)
    return(currentPlayer)

def move():
  dataType = "number"
  column=validCheck(dataType)
  return (column)

def checkMove(column, currentPlayer):
    for row in range(6):
      print(row,column)
      grid[1:column] = currentPlayer
      #if grid[1:column] == "-":
         # print("Cock")
          #grid[1:column] = currentPlayer
    displayGrid()
        
#Start of Program
currentPlayer = menu()
column = move()
checkMove(column, currentPlayer)

#print (currentPlayer)
print("END OF PROGRAM")

#James Worley and Tom Comrie 09/09/2020