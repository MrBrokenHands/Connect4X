#Grid
grid = [["-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-"], ["-", "-", "-", "-", "-", "-", "-"]]

#grid = [["-"] * 7] * 6 #broken who tf knows

def displayGrid():
  print("\n" * 1000)
  count = 0
  for x in range(6):
    print(grid[count])
    print()
    count = count + 1

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
  print("It's",currentPlayer,"'s Turn!'")
  column=validCheck(dataType)
  return (column)

def makeMove(column, currentPlayer):
  moveDone = False
  while moveDone == False:
      count = 5
      for x in range (6):
          if grid[0][column] == "R" or grid[0][column] == "Y":
            displayGrid()
            print("That column is full!")
            column = move()
            column = column - 1
          elif grid[count][column] == "-":
            grid[count][column] = currentPlayer
            break
          else:
            count = count - 1
      moveDone = True
  displayGrid()

def checkWinner():
  
        
#Start of Program
winCondition = False
currentPlayer = menu()
while winCondition == False:
  column = move()
  column = column - 1
  makeMove(column, currentPlayer)
  if currentPlayer == "R":
    currentPlayer = "Y"
  elif currentPlayer =="Y":
    currentPlayer = "R"


#print (currentPlayer)
print("END OF PROGRAM")

#James Worley and Tom Comrie 09/09/2020