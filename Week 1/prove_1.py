import math
def tire_volume():
    w= int(input("Enter the width of the tire in mm (ex 205): "))
    a = int(input("Enter the aspect ratio of the tire (ex 60): "))
    d = int(input("Enter the diameter of the tire in inches (ex 15): "))
    prepar = int(math.pi*a*(w**2))
    par = int(w * a +(2540*d))
    volume =  (prepar * par)/10000000000

    print("The approximate volume is "+ str(round(volume,2)) + "liters")

tire_volume()