#This program will ask for the users age and give them the range where they should keep
# there heart rate for best strengthening abilities
print("Welcome! I'm happy you're wanting to strengthen your heart.")
age = input("to begin, What is your age? ")
heartmax = (220-int(age))
low = heartmax * .65
high = heartmax * .85

print("Perfect! When you excercise you should keep your heart beat between", str(low) + " and " + str(high))
print("beats per minute to strenghten your heart the best!")