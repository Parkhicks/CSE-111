import math
from datetime import datetime

def tire_volume():
    w= int(input("Enter the width of the tire in mm (ex 205): "))
    a = int(input("Enter the aspect ratio of the tire (ex 60): "))
    d = int(input("Enter the diameter of the tire in inches (ex 15): "))
    prepar = int(math.pi*a*(w**2))
    par = int(w * a +(2540*d))
    volume =  (prepar * par)/10000000000
    current_date = datetime.now()
    current_date = f"{current_date:%Y-%m-%d}"


    print("Today is: " + str(current_date))
    print("The approximate volume is "+ str(round(volume,2)) + " liters")

    with open("tire_volume.txt", "at" ) as doc:
        print(str(current_date) + ", Width = " + str(w) + ", Aspect = " + str(a) + ", Diameter = " + str(d) + ", Volume = " + str(round(volume,2)), file=doc)

tire_volume()


