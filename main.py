import os
import datetime

day = datetime.date.today().strftime('%d')
month = datetime.date.today().strftime('%m')
year = datetime.date.today().strftime('%Y')
path = f"/home/abdelrahman/Documents/Diary/{year}/{month}"
file_path = os.path.join(path, f"{day}.txt")

def add_entry():
   
    os.makedirs(path, exist_ok=True )
    

    content = input("What are you feeling today? \n")
    with open(file_path, "a") as file:
        file.write(content + "\n")

    return
def show_entry():

    iYear = input("What year? : ")
    iMonth = input("What month? : ")
    iDay = input("What day? : ")
    ipath = f"/home/abdelrahman/Documents/Diary/{iYear}/{iMonth}/{iDay}.txt"

    if (os.path.exists(ipath)):
        with open(ipath, "r") as file:
          content =  file.read()
        print(content)  
    else:
        print("Whoops please enter a valid path") 
        print(ipath)     



    return

def main():
    while True:
        print(str(datetime.date.today()))
        print("---- Welcome to your Diary ----")
        print("Choose and option:\n 1. Create an entry\n 2. Show an entry\n 3. Exit")
        option = int(input("Option : "))
        if option == 1:
            add_entry()
            
        elif option == 2:
            show_entry()
            
        elif option == 3:
            break
        else:
            print("Whoops invalid input. Choose a valid input")
        

if __name__ == "__main__":
    main()