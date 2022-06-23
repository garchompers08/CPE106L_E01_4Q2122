def primary():
     #inputFN = input("Enter the file name: " )

     with open(r"C:\Users\patri\Documents\3rd Year\4th Sem\CPE106L\LR\LR1\P2\CPE106L_E01_4Q2122\LR1\text.txt", 'r') as fp:
          num_lines = sum(1 for line in fp)
          print('Total lines:', num_lines) # 8
    

     if num_lines!=0:
          print("Enter Value: ")
          quotes=input()
          print(quotes[num_lines])
     else:
          print("You have exited the program :)")


if __name__== "__main__":
  primary()

