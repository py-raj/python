print("Wellcome to the number guessing game.")
print("Try to guess the number in 10 attempts.")
attempt = 0
def all():
    import random
    
    try:
        a = int(input("Enter the minimum range of number in a game : "))
        b = int(input("Enter the maximum range of number in a game : "))
        rno = random.randint(a,b)
    except:
        print("somthing went wrong \n try again")
        all()
            
        # global attempt
        # attempt = attempt + 1

    def num():
        num1 = int(input("Enter your guess no : "))
        if (attempt > 2):
            print("you lose")   
        elif (num1 == rno):
            print(f"Congratulations you win. \nthe secret no is {rno}")
        elif (num1 > b):
            print(f"Enter number in range of {a} to {b}")
            num()
        elif (num1 < a):
            print(f"Enter number in range of {a} to {b}")
            num()
        else:
            print("Try again")
            num()
    num()
    def pa():
        playagain = input("Do you want to play this game agian (yes/no) : ")  
        if (playagain.lower() == "yes") :
            print("\n")
            # attempt = 0
            all()
    pa()        
all()
print("Thanks for playing the game")
