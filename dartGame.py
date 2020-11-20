import time 
from random import *

def game():

    score = 301
    dart_count = 0
    while score > 0:

        randnum = randint(1, 5)

        begin = time.time()

        timer = input("Please enter to stop the timer ")

        end = time.time()
        elapsed = end - begin
        elapsed = int(elapsed)

        print(f"The time elapsed after {elapsed} seconds")

        if randnum == elapsed:
            print("You scored 100")
            score = score - 100
        elif randnum == elapsed - 1 or randnum == elapsed + 1:
            print("You scored 50")
            score = score - 50
        elif randnum == elapsed - 2 or randnum == elapsed + 2:
            print("You scored 20")
            score = score - 200
        else:
            print('You missed..')
        print()
        dart_count += 1

    print(f"You threw {dart_count} darts")
    print()
    return dart_count


p1 = input("Enter player one ")
p2 = input("Enter player two ")

dart_countp1 = game()

dart_countp2 = game()

print("Lowest Socre wins the game")
print()
print(f"{p1}'Player 1 threw, {dart_countp1} darts")
print()
print(f"{p2} Player 2 threw, {dart_countp2} darts")
print()

if dart_countp1 > dart_countp2:
    print(p1, "is the winner ")

elif dart_countp2 > dart_countp1:
    print(p2," is the winner")

else:
    print(" Drawwww")