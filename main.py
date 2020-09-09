#Grid
grid = [["-" * 7] * 6]

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
          valid = True
        except:
          print("Input is not a valid",dataType)
      elif dataType == "colour":
        try:
          check = ""
          check = str(input("Pick a Colour (R or Y)\n"))
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
            print("111Input is not a valid",dataType) #needs fixing int
            valid = False
            continue
        except:
          continue #needs fixing str
    break
  return(check)
  
#Menu
def menu(): 
    print("Connect 4 - Press the enter key to play")
    input()
    dataType = "colour"
    currentPlayer = str(input("Red or Yellow?")) #Either set as "Y" or "R"
    validCheck(currentPlayer)
    print("currentPlayer")
    currentPlayer = ""

def move():
  dataType = "number"
  validCheck(dataType)

def checkMove(column):
    for row in range(6):
      if grid[row:column] == "-":
          grid[row:column] = currentPlayer
    print(grid)
        

#menu()
column=move()
checkMove(column)
print("END OF PROGRAM")

#James Worley and Tom Comrie 09/09/2020