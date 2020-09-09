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
          check = int(input("Pick a Column (1-7)"))
          valid = True
        except:
            print("coon")
      elif dataType == "colour":
        try:
          check = ""
          check = str(input("Pick a Colour"))
          valid = True
        except:
            print("Please enter a ", dataType, " (R or Y)")
      try:
        if check >= 1 and check <= 7:
          break
        else:
          print("Input is not valid ", dataType)
          valid = False
          continue
      except:
        print("Input is not valid ", dataType)
    break
  return(check)
  
#Menu
def menu(): 
    print("Connect 4 - Press the enter key to play")
    input()
    currentPlayer = str(input("Red or Yellow?")) #Either set as "Y" or "R"

def move():
  validCheck()
  '''
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
  '''

def checkMove(column):
    for row in range(6):
      print(row)
      if grid[row, column] == "-":
          grid[row, column] = currentPlayer
        

#menu()
column=move()
checkMove(column)
print("END OF PROGRAM")

#James Worley and Tom Comrie 09/09/2020