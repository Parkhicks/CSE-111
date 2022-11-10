one=1
two=1
three=1
four=1
five=1
six=1
seven=1
eight=1
nine=1
ten=1
score=0

print("Welcome to the Rosenberg self esteem assessment.\nPlease answer these statements with the following\nresponses.")
print("Strongly Disagree: D \ndisagree: d:  \nAgree: A \nStrongly Agree: a")

#Question #1
one = input("I feel that I am a person of worth, at least on an equal plane with others: ")
if one == ("a") or ("A") or("D") or("d"):
    if one == ("A"):
        score += 3
    elif one ==("a"):
        score += 2
    elif one ==("D"):
        score += 0
    elif one ==("d"):
        score += 1
else:
    print("Incorrect option, please enter it again.")
    one = input("I feel that I am a person of worth, at least on an equal plane with others: ")
    
    
#Question #2
two = input("I feel that I have a number of good qualities: ")
if two ==("a") or ("A") or("D") or("d"):
    if two == ("A"):
        score += 3
    elif two ==("a"):
        score += 2
    elif two ==("D"):
        score += 0
    elif two ==("d"):
        score += 1
else:
    print("Incorrect option, please enter it again.")
    two = input("I feel that I have a number of good qualities: ")

#Question #3
three = input("All in all, I am inclined to feel that I am a failure: ")
if three ==("a") or ("A") or("D") or("d"):
    if three == ("A"):
        score += 0
    elif three ==("a"):
        score += 1
    elif three ==("D"):
        score += 3
    elif three ==("d"):
        score += 2
else:
    print("Incorrect option, please enter it again.")
    three = input("All in all, I am inclined to feel that I am a failure: ")
    
    
#Question #4
four = input("I am able to do things as well as most other people: ")
if four ==("a") or ("A") or("D") or("d"):
    if four == ("A"):
        score += 3
    elif four ==("a"):
        score += 2
    elif four ==("D"):
        score += 0
    elif four ==("d"):
        score += 1
else:
    print("Incorrect option, please enter it again.")
    four = input("I am able to do things as well as most other people: ")



#Question #5
five = input("I feel I do not have much to be proud of: ")
if five ==("a") or ("A") or("D") or("d"):
    if five == ("A"):
        score += 0
    elif five ==("a"):
        score += 1
    elif five ==("D"):
        score += 3
    elif five ==("d"):
        score += 2
else:
    print("Incorrect option, please enter it again.")
    five = input("I feel I do not have much to be proud of: ")
    
    
#Question #6
six = input("I take a positive attitude toward myself: ")
if six ==("a") or ("A") or("D") or("d"):
    if six == ("A"):
        score += 3
    elif six ==("a"):
        score += 2
    elif six ==("D"):
        score += 0
    elif six ==("d"):
        score += 1
else:
    print("Incorrect option, please enter it again.")
    six = input("I take a positive attitude toward myself: ")


#Question #7
seven = input("On the whole, I am satisfied with myself: ")
if seven ==("a") or ("A") or("D") or("d"):
    if seven == ("A"):
        score += 3
    elif seven ==("a"):
        score += 2
    elif seven ==("D"):
        score += 0
    elif seven ==("d"):
        score += 1
else:
    print("Incorrect option, please enter it again.")
    seven = input("On the whole, I am satisfied with myself: ")
    
    
#Question #8
eight = input("I wish I could have more respect for myself: ")
if eight ==("a") or ("A") or("D") or("d"):
    if eight == ("A"):
        score += 0
    elif eight ==("a"):
        score += 1
    elif eight ==("D"):
        score += 3
    elif eight ==("d"):
        score += 2
else:
    print("Incorrect option, please enter it again.")
    eight = input("I wish I could have more respect for myself: ")


#Question #9
nine = input("I certainly feel useless at times: ")
if nine ==("a") or ("A") or("D") or("d"):
    if nine == ("A"):
        score += 0
    elif nine ==("a"):
        score += 1
    elif nine ==("D"):
        score += 3
    elif nine ==("d"):
        score += 2
else:
    print("Incorrect option, please enter it again.")
    nine = input("I certainly feel useless at times: ")
    
    
#Question #10
ten = input("At times I think I am no good at all: ")
if ten ==("a") or ("A") or("D") or("d"):
    if ten == ("A"):
        score += 0
    elif ten ==("a"):
        score += 1
    elif ten ==("D"):
        score += 3
    elif ten ==("d"):
        score += 2
else:
    print("Incorrect option, please enter it again.")
    ten = input("At times I think I am no good at all: ")

print("\nThanks for your time responding to the questions\nYour Score is: " + str(score))
print("If your score is lower than 15 points, the person may have a problematic low self-esteem.")



