print("NAME: Haneesh M")
print("USN:1AY24AI038")
print("SECTION:M")

import random
guess = ''
while guess not in ('heads'.'tails'):
                    print("Guess the coin toss! Enter heads ot tails: ")
                    guess = input()
                    break
toss = random.randint(0,1)
if toss==guess:
    print("You got it")
else:
    print("NOPE!!! Guess again! ")
    guess = input()
    if toss==guess:
        print("You got it")
    else:
        print("Nope, you did not get this")
