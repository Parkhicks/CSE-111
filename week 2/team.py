from datetime import datetime
def discount():
    subtotal = float(input("What is the subtotal for your purchase today? "))
    day = datetime.today().weekday()
    day = 2
    if day == 1 or 2 and subtotal > 50 :
        discount = round(subtotal*.1,2)
        total  = (subtotal*.9) * 1.06
        tax = subtotal*.9 *.06
    else:
        discount = 0
        total = subtotal * 1.06
        tax = total-subtotal
    print("Your discount is: $" + str(discount))
    print ("Your total tax for today is: $" + str(round(tax,2)))
    print("Your total is: $ " + str(round(total,2)))

discount()