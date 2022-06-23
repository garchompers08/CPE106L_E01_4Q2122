def primary():
     inputFN = input("Enter the file name: " )

     with open(r"text.txt", 'r') as fp:
          num_lines = sum(1 for line in fp)
          print('Total lines:', num_lines) # 8
    

     if inputNum!=0:
          f = open("text.txt")
          quotes = f.readlines()
          f.close()
          print(quotes[inputNum-1])
     else:
          print("You have exited the program :)")


if __name__== "__main__":
  primary()