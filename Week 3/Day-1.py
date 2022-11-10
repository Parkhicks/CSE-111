w = 0
l = 0
def amount():
    amount = input("How many rectangles do you have? ")
    return int(amount)
def calc_area():
    area = area + (w*l)
    return int(area)
def user_input():
    w = ("Enter the width of the rectangle: ")
    l = ("Enter the length of the rectangle: ")
    calc_area()

def main():
    area = 0
    for i in range(amount):
        user_input()
    print(calc_area)

main()