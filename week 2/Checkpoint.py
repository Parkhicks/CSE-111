import math
def boxes():
    quantity = int(input("How many manufactured items do you want to pack? "))
    boxes = int(input("How many items will you pack in each box? "))
    boxes_needed = math.ceil(float(quantity/boxes))
    print ("You'll need " + str(boxes_needed) + " boxes, to pack " + str(quantity) + " items.")

boxes()
