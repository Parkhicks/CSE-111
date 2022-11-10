cont ="Y"
family = []
counter = 0

while cont == "Y":
    name = input("What is the first name of a family member? ")
    age = input("What is the age of that fmaily member? ")
    cont= input("Would you want to add another family member? (Y or N) ")

    family.append({"name": name, "age": age})

with open ("family.txt" , "at") as family_file:
    print (family,file=family_file)

p =input("Would you like to print a list of your family members? ")
if p == "Y":
    print (family)

#edit = input("Would you want to edit a family member? ")

family.pop(1)
P_1 = input("What is the first name of a family member? ")
a_1= str(input("What is the age of that fmaily member? "))
family.insert{"name": P_1, "age": a_1},1
print (family)
