# Challenge one: How many commands in one line? 6
# print(float(abs(round(-2850984.87231,3)))/int(input("Enter a number here ")

#Challenge two: Call print with five arguments
#print("the dog,",sep="-", end="ate the cat",file=sys.stdout,flush=False)

#Challenge three: Do this equation
#def random_math():
    #import math
    #value = (round((17**9),0)/3) - 6
    #if value % 2 == 0 :
        #return  "True"
    #else:
        #return  "False"
#print(random_math())

#Challenge four, import random, make list of numbers, sor it
#import random
#for i in range(0,20):
    #numbers.append(random.randint(0,100))
#numbers.sort()
#print(numbers)


#Challenge five: even minute print even minute

import time
now = datetime.now()
display_message = "even minute"
if (now.minute % 2 > 0):
    display_message = "Odd minute"
