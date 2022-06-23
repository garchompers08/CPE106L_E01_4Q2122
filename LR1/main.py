
def primary():
     inputFN = input("Enter the file name: " )

    with open(r"E:\demos\files\read_demo.txt", 'r') as fp:
    for count, line in enumerate(fp):
        pass
    print('Total Lines', count + 1)
    

     if inputNum!=0:
          f = open("text.txt")
          quotes = f.readlines()
          f.close()
          print(quotes[inputNum-1])
     else:
          print("You have exited the program :)")


if __name__== "__main__":
  primary()