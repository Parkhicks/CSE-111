alist = []

def add_list_behind():
    item = input("What do you want to add to the list? ")
    alist.append(item)
def add_list_anywhere():
    item = input("What do you want to add to the list? ")
    spot = int(input("Which item do you want the item to be added in? "))
    alist.insert(spot-1,item)
def remove_item():
    remove = input("Which item do you want to remove from the list? ")
    alist.remove(remove)

for i in range (5):
    add_list_behind()
    add_list_anywhere()
    print(alist)
    remove_item()
    print(alist)