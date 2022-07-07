def primary():
     inputFN = input("Enter the file name [include .txt]: " )
     line_assign = int(input("Enter the number of lines you wish to put in the .txt file: "))
     lines = []

     if(line_assign != 0):
          f = open(inputFN, "w+")
          

          for i in range(line_assign):
               arr = input()
               lines.append(arr)

          for i in range(line_assign):
               f.write(lines[i])
               f.write("\n")
          
          f = open(inputFN, "r")
          readline = f.readlines()

          print("\n\nThe inputted lines are: \n")

          for y in range(line_assign):
               print(readline[y])
          
          f.close()

          print("Please pick a line number from the list of lines shown above: ")
          EnterVal = int(input())
          
          if EnterVal!=0 and EnterVal > line_assign:
               print("The inputted line number must be between 1 and ", line_assign)
               
          elif EnterVal!=0 and EnterVal<= line_assign:
                    f = open(inputFN,"r")
                    quotes = f.readlines()
                    print("Line","[",EnterVal, "]:",quotes[EnterVal-1])
                    f.close()
          else:
                    print("You have exited the program :)")
     else:
          print("You have exited the program :)")
     
          
    
if __name__== "__main__":
  primary()

