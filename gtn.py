#Number guessing game
import random, time

game = True

while game == True:
    print("Welcome to Crypza's number guessing game")
    time.sleep(1)
    while True:
        print('''
        Menu
        
        1. Play game
        
        2. Exit
        
        ''')
        try:
            menuC = int(input("Choose an alternative: "))
            time.sleep(0.3)
        except ValueError:
            print('''That's not an alternative...
            
        
            ''')
            time.sleep(3)
            break

        if menuC == 1:
            print("Ok, let's play!")
            compC = random.randint(0,10)
            time.sleep(1)
            print("I have now chosen a number between 0 and 10... try and guess")
            gameActive = True
            while gameActive == True:
                try:
                    playerC = int(input("Your guess is: "))
                    time.sleep(0.3)
                except:
                    print("That wasnt an option, so we assume you meant 1")
                    playerC = 1
                    time.sleep(0.3)
                if playerC > 10 or playerC < 0:
                    print("It's something between 0 and 10... try again")
                    time.sleep(0.3)
                elif playerC == compC:
                    print("You guessed right!")
                    time.sleep(0.3)
                    gameActive = False
                elif playerC > compC:
                    print("Too high!")
                    time.sleep(0.3)
                elif playerC < compC:
                    print("Too low!")
                    time.sleep(0.3)
                else:
                    print("Whoops, something went wrong... try again")
                    time.sleep(0.3)
        elif menuC == 2:
            print("Ok, come back soon!")
            time.sleep(1)
            exit()
        else:
            print("Whoops, something went wrong... try again")
            time.sleep(0.3)

