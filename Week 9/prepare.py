
provinces = open("provinces.txt", "r")
read = provinces.readlines()
modified = []

for line in read:
    modified.append(line.strip())

print (modified)

del modified[0]
index = len(modified)-1
del modified[index]
print (modified)

place = 1
for item in modified :
    if item == "AB" :
        del modified[(place-1)]
        modified.insert((place-2), "Alberta" )
    place = place+1

print (modified)

counts = 0
for item in modified:
    if item == "Alberta":
        counts = counts + 1
print("Alberta occurs "+ str(counts) + " times in the modified list. ")