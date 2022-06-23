def primary():
     inputFN = input("Enter the file name: " )

     if inputFN == "quotes1":
          with open(r"G:\MAPUA\2nd Year\4th Term\CPE106L\Module 1\LR1 PP\CPE106L_E01_4Q2122\LR1\quotes1.txt", 'r') as fp:
          
               for count, line in enumerate(fp):
                pass
          num_lines = count+1
          print('Total lines:', num_lines) # 8
     
          EnterVal = int(input("Enter Value to select a line: "))

          if EnterVal!=0:
               f = open(r"G:\MAPUA\2nd Year\4th Term\CPE106L\Module 1\LR1 PP\CPE106L_E01_4Q2122\LR1\quotes1.txt","r")
               quotes = f.readlines()
               print(quotes[EnterVal-1])
               f.close()
          else:
               print("You have exited the program :)")

     elif inputFN == "quotes2":
          with open(r"G:\MAPUA\2nd Year\4th Term\CPE106L\Module 1\LR1 PP\CPE106L_E01_4Q2122\LR1\quotes2.txt", 'r') as fp:
               for count, line in enumerate(fp):
                    pass
          num_lines = count+1
          print('Total lines:', num_lines) # 8
     
          EnterVal = int(input("Enter Value to select a line: "))

          if EnterVal!=0:
               f = open(r"G:\MAPUA\2nd Year\4th Term\CPE106L\Module 1\LR1 PP\CPE106L_E01_4Q2122\LR1\quotes2.txt","r")
               quotes = f.readlines()
               print(quotes[EnterVal-1])
               f.close()
          else:
               print("You have exited the program :)")

     elif inputFN == "quotes3":
          with open(r"G:\MAPUA\2nd Year\4th Term\CPE106L\Module 1\LR1 PP\CPE106L_E01_4Q2122\LR1\quotes3.txt", 'r') as fp:
               for count, line in enumerate(fp):
                    pass
          num_lines = count+1
          print('Total lines:', num_lines) # 8
          
          EnterVal = int(input("Enter Value to select a line: "))

          if EnterVal!=0:
               f = open(r"G:\MAPUA\2nd Year\4th Term\CPE106L\Module 1\LR1 PP\CPE106L_E01_4Q2122\LR1\quotes3.txt","r")
               quotes = f.readlines()
               print(quotes[EnterVal-1])
               f.close()
          else:
               print("You have exited the program :)")
     
     else:
          print("That file does not exist")


    
if __name__== "__main__":
  primary()

