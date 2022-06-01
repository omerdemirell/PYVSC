import random
import time

"""
Roll 2 dice and the program will stop when both dice have a value of 6.
Now let's write a program that tells how many times the dice are rolled until both dice come up with 6s.
"""


"""
The reason for the 'random' method I use inside the loop is because I want to generate random numbers in a certain range.
The reason I want to use 'randint' is because I want to return random integers including both endpoints.
"""

i = 1
while True:
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    
    if dice_1 == 6 and dice_2 ==6:
        print(""""Trial {}:\t({},{}) """.format(i, dice_1, dice_2))
        time.sleep(2)
        break
    
    print(""""Trial {}:\t({},{}) """.format(i, dice_1, dice_2))
    i += 1
    time.sleep(0.5)
    
print("""\n {}th try (6,6) Came""".format(i))
    
    
def generate():
    while True:
        yield random.randint(1,6), random.randint(1,6)
        time.sleep(.1)
        
c = 1
for i, j in generate():
    if i == j ==6:
        print(f"Found: {c}")
        break
    else:
        print(f'Try: {c}', end='\r')
        c +=1
                
        


                                                     
    



