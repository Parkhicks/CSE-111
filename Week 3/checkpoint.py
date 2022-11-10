from types import MappingProxyType

end_od = 0
beg_od = 0
fuel = 0
mpg = 0
lp100k = 0
def miles_per_gallon(beg_od,end_od,fuel):
    distance = end_od - beg_od 
    return (distance/fuel)



def lp100k_from_mpg(mpg):
    lp100k =  (235.215)/mpg
    return lp100k


def main():
    beg_od = float(input("Enter the beggining odometer reading: "))
    end_od = float(input("Enter the ending odometer reading: "))
    fuel = float(input("Enter the amount of gas used: "))
    mpg = miles_per_gallon(beg_od,end_od,fuel)
    lp100k = lp100k_from_mpg(mpg)
    print ("The efficiency for that trip is: " + str(round(float(mpg,),2)) + " miles per gallon, or " + str(round(float(lp100k),2)) + " liters per 100km.")

main()