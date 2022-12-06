import csv
import math
print()
"""
def main():
    processed = "start"
    print("Welcome to the Automated Construction Take-off Calculator, this program is designed with a couple options of getting data\nyou can either reference different documents with the quantities prewritten into them. These can be either .txt or .csv files.")
    print("Second, we can go through all the phases of the construction process and ask you to enter the quantities manually. After retrieving\nthe quantities either by reference or input we'll go through it again and ask for the price, or ask for a file with prices.")
    while processed != "file" or processed != "manual":
        quantities = input("To begin do you have a .txt or .csv file with the written product and the quantitiy of them? or would you like to enter \nthem manually? type either 'file' or 'manual' ")
        processed = quantities.strip()
        processed = processed.lower()
        if processed != "file" or processed != "manual":
            print("Invalid input, please enter either 'file' or 'manual' ")
        elif processed =="file":
            files_q()
        elif processed =="manual":
            inputted_q()
"""

#creating empty dictionaries for all the values that program will return to the user stored so they can be written to a file later on 
foundation_dict ={}
walls_dict={}
flooring_dict={}
fixtures_dict={}
roofing_dict={}


    
def inputted_q():
    #the function that is going to manually ask them questions to get quantities
    print("\nSounds good, we'll go through asking you questions to get quantities.")
    foundation()
    price_foundation()
    #flooring()
    #price_flooring()
    walls()
    price_walls()
    fixtures()
    price_fixtures()
    roofing()
    price_roofing()

# all functions defined to get the required quantities and prices from the user

#foundations and cost of foundation
def foundation():
    #tested & working 12/01/2022
    def yardage(length,width,height):
        f_width = width/12
        f_height = height/12
        yards = math.ceil((f_height * f_width * length)/27)
        return yards
    print("Awesome we'll start with the footings then move to the foundation. ")
    l_feet = input("What is the total linear feet of the foundation area (Usually the perimeter but its the total length of all concrete walls) ")
    l_foot_feet = input("What is the total linear feet of the footings? (Usually the same as the total linear feet of the foundation unless you have isolated pier footings then you just add the length of those. ")
    h_foo = input("What is the total height of the footings in inches? ")
    t_foo = input("What is the total thickness of the footings  in inches? ")
    h_found = input("What is the total height of the foundation walls in inches? ")
    t_found = input("What is the total thickness of the foundation walls in inches? ")
    yard_foo = yardage(int(l_foot_feet),int(t_foo),int(h_foo))
    yard_found = yardage(int(l_feet),int(t_found),int(h_found))
    m_sill = math.ceil(int(l_feet) /12)
    anchor_b = math.ceil(int(l_feet)/6)
    foundation_dict["footing yardage"] = yard_foo
    foundation_dict["foundation yardage"] = yard_found
    foundation_dict["mud sill"] = m_sill
    foundation_dict["anchor bolts"] = (anchor_b+4)

    print("\nThe total cubic yards of concrete needed for the footings is: "+ str(yard_foo))
    print("The total cubic yards of concrete needed for the footings is: "+ str(yard_found))
    print(f"You'll need {m_sill}  2'x 4''x 12's for all the mudsill plates.")
    print(f"You'll also need {anchor_b}-{int(anchor_b)+4} anchor bolts to finish off the foundation")
def price_foundation():
    conc_cost =float(input("\nWhat is the price of a yard of concrete? "))
    mud_sill_cost = float(input("What is the price of a single 2'x4'x12''? "))
    anchor_cost = float(input("What is the price of one anchor bolt? "))
    quantity = foundation_dict.get("footing yardage")
    foundation_dict["footing yardage"] =[quantity,conc_cost]
    quantity = foundation_dict.get("foundation yardage")
    foundation_dict["foundation yardage"] =[quantity,conc_cost]
    quantity = foundation_dict.get("mud sill")
    foundation_dict["mud sill"] =[quantity,mud_sill_cost]
    quantity = foundation_dict.get("anchor bolts")
    foundation_dict["anchor bolts"] =[quantity,anchor_cost]
    

#flooring and cost of flooring
#def flooring():
#def price_flooring():


#walls and cost of walls
def walls():
    l_feet_ext = int(input("What is the total linear feet of all the exterior walls? "))
    l_feet_int = int(input("What is the total linear feet of all the interior walls? "))
    w_h = int(input("What is the height of the ceilings? (in feet) "))
    stud_height = (w_h*12)
    l_feet = l_feet_int + l_feet_ext
    plates_lb = ((l_feet_ext * 3)/12)
    plates_nlb = ((l_feet_int * 2)/12)
    plates = math.ceil(plates_lb+plates_nlb)
    insulation = math.ceil(((l_feet_ext/ 1.3333) * w_h)/32)
    studs = l_feet
    ext_sheeting = math.ceil((l_feet_ext*w_h) /32)
    int_sheeting = math.ceil((((l_feet_ext*w_h) /32)+ ((l_feet_int*w_h*2) /32)))

    print(f"\nFor all the plates (sole, top, and cap (where needed)) you'll need {plates} 2'x 4''x 12's ")
    print(f"You'll need approximately {studs} 2'x 4''x  {(w_h*12 -3.375)}''s for all the studs ")
    print(f"You'll need {insulation} rolls of 15''x 32' fiberglass insulation to insulate all exterior walls ")
    print(f"You'll need {ext_sheeting} sheets of 1/2'' thick OSB plywood  (4'x10' sheets) ")
    print(f"You'll need {int_sheeting} sheets of 5/8'' thick Gypsum board (typical 4'x8' sheets) ")
    walls_dict["plates"] = plates
    walls_dict["studs"] = studs
    walls_dict["insulation"] = insulation
    walls_dict["exterior sheeting"] = ext_sheeting
    walls_dict["interior sheeting"] = int_sheeting
def price_walls():
    plate_cost = float(input("What is the price of a 2'x4'x12''? "))
    stud_cost = float(input("What is the price of a 2'x4'x12''? "))
    insulation_cost = float(input("What is the price of 15' 32'' roll of fiberglass insulation? "))
    ext_cost = float(input("What is the price of a 1/2'' thick OSB plywood? "))
    int_cost = float(input("What is the price of a 5/8'' thick gypsum board? "))
    quantity = walls_dict.get("plates")
    walls_dict["plates"] =[quantity,plate_cost]
    quantity = walls_dict.get("studs")
    walls_dict["studs"] =[quantity,stud_cost]
    quantity = walls_dict.get("insulation")
    walls_dict["insulation"] =[quantity,insulation_cost]
    quantity = walls_dict.get("exterior sheeting")
    walls_dict["exterior sheeting"] =[quantity,ext_cost]
    quantity = walls_dict.get("interior sheeting")
    walls_dict["interior sheeting"] =[quantity,int_cost]


#fixtures and cost of fixtures
def fixtures():
    doors = input("How many doors are you going to have? (both interior & exterior) ")
    windows =input("How many windows are you going to have? ")
    fixtures_dict["doors"]= doors
    fixtures_dict["windows"] = windows
def price_fixtures():
    door_cost = float(input("What is the cost of a door? "))
    win_cost = float(input("What is the cost of a window? "))
    quantity = fixtures_dict.get("doors")
    fixtures_dict["doors"] = [quantity,door_cost]
    quantity = fixtures_dict.get("windows")
    fixtures_dict["windows"] = [quantity,win_cost]


#roofing and cost of roofing
def roofing():
    have = input("Do you know the surface area of the roof? (Y or N) ")
    roof_length = input("What is the length of the area you are going to have a roof over? (in feet) ")
    roof_width = input("What is the width of the area you are going to have a roof over? (in feet) ")
    if have.lower() == "n":
        slope = input("What is the rise of the roof in inches per foot? ")
        slope_frac = math.sqrt((slope**2) + (12**2))
        area = roof_length*roof_width
        surface_area = area*slope_frac
        squares = surface_area/100
    elif have.lower()=="y":
        surface_area=input("What is the surface are of the roof? ")
        squares = surface_area/100

    if roof_length >= roof_width:
        run = roof_width
    elif roof_length <= roof_width:
        run = roof_length    

    trusses = (run/2) +1
    print(f"You'll need {trusses} of trusses to build your roof")
    print(f"You'll need {squares} of shingles to cover your roof") 
    roofing_dict["trusses"] = trusses
    roofing_dict["shingle squares"] = squares
def price_roofing():
    truss_cost = float(input("What is the cost of a truss? "))
    square_shingle_cost = float(input("What is the cost of a square of shingles? "))
    quantity = roofing_dict.get("trusses")
    roofing_dict["trusses"] = [quantity,truss_cost]
    quantity = roofing_dict.get("shingle squares")
    fixtures_dict["shingle squares"] = [quantity,square_shingle_cost]


def files_q():
    #the function that is going to ask for a file with the quantities and pull form there. Will also have them look over the list and see if they want to add anything
    print("Congratulations, we're getting your file now.")


#foundation()
#price_foundation()
#print(foundation_dict)
