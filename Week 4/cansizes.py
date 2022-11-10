import math
    
def compute_volume(radius,height):
    return (math.pi *(radius**2)*height)
    
def compute_surface_area(radius,height):
    return (2*math.pi *(radius+height))

def efficency(volume,surface_area):
    return (volume/surface_area)



radius=6.83
height=10.16
cost=0.28
volume=compute_volume(radius,height)
surface_area=compute_surface_area(radius,height)
ef =efficency(volume,surface_area)
print("Can #1 Volume: "+ str(round(volume,2)) +" + surface area: "+ str(round(surface_area,2))+ "Efficency: "+str(round(ef,2)) +" cost: "+str(round(cost,2)))
print()
radius=7.78
height=11.91
cost=0.43
volume=compute_volume(radius,height)
surface_area=compute_surface_area(radius,height)
ef =efficency(volume,surface_area)
print("Can #2 Volume: "+ str(round(volume,2)) +" + surface area: "+ str(round(surface_area,2))+ "Efficency: "+str(round(ef,2)) +" cost: "+str(round(cost,2)))
print()
radius=8.73
height=11.59
cost=0.45
volume=compute_volume(radius,height)
surface_area=compute_surface_area(radius,height)
ef =efficency(volume,surface_area)
print("Can #3 Volume: "+ str(round(volume,2)) +" + surface area: "+ str(round(surface_area,2))+ "Efficency: "+str(round(ef,2)) +" cost: "+str(round(cost,2)))
print()
radius=10.32
height=11.91
cost=0.61
volume=compute_volume(radius,height)
surface_area=compute_surface_area(radius,height)
ef =efficency(volume,surface_area)
print("Can #4 Volume: "+ str(round(volume,2)) +" + surface area: "+ str(round(surface_area,2))+ "Efficency: "+str(round(ef,2)) +" cost: "+str(round(cost,2)))
print()
radius=10.79
height=17.78
cost=0.86
volume=compute_volume(radius,height)
surface_area=compute_surface_area(radius,height)
ef =efficency(volume,surface_area)
print("Can #5 Volume: "+ str(round(volume,2)) +" + surface area: "+ str(round(surface_area,2))+ "Efficency: "+str(round(ef,2)) +" cost: "+str(round(cost,2)))
print()
radius=13.02
height=14.29
cost=0.83
volume=compute_volume(radius,height)
surface_area=compute_surface_area(radius,height)
ef =efficency(volume,surface_area)
print("Can #6 Volume: "+ str(round(volume,2)) +" + surface area: "+ str(round(surface_area,2))+ "Efficency: "+str(round(ef,2)) +" cost: "+str(round(cost,2)))
print()
radius=5.40
height=8.89
cost=0.22
volume=compute_volume(radius,height)
surface_area=compute_surface_area(radius,height)
ef =efficency(volume,surface_area)
print("Can #7 Volume: "+ str(round(volume,2)) +" + surface area: "+ str(round(surface_area,2))+ "Efficency: "+str(round(ef,2)) +" cost: "+str(round(cost,2)))
print()
radius=6.83
height=7.62
cost=0.26
volume=compute_volume(radius,height)
surface_area=compute_surface_area(radius,height)
ef =efficency(volume,surface_area)
print("Can #8 Volume: "+ str(round(volume,2)) +" + surface area: "+ str(round(surface_area,2))+ "Efficency: "+str(round(ef,2)) +" cost: "+str(round(cost,2)))
print()
radius=15.72
height=17.78
cost=1.53
volume=compute_volume(radius,height)
surface_area=compute_surface_area(radius,height)
ef =efficency(volume,surface_area)
print("Can #9 Volume: "+ str(round(volume,2)) +" + surface area: "+ str(round(surface_area,2))+ "Efficency: "+str(round(ef,2)) +" cost: "+str(round(cost,2)))
print()
radius=6.83
height=12.38
cost=0.34
volume=compute_volume(radius,height)
surface_area=compute_surface_area(radius,height)
ef =efficency(volume,surface_area)
print("Can #10 Volume: "+ str(round(volume,2)) +" + surface area: "+ str(round(surface_area,2))+ "Efficency: "+str(round(ef,2)) +" cost: "+str(round(cost,2)))
print()
radius=7.62
height=11.27
cost=0.38
volume=compute_volume(radius,height)
surface_area=compute_surface_area(radius,height)
ef =efficency(volume,surface_area)
print("Can #11 Volume: "+ str(round(volume,2)) +" + surface area: "+ str(round(surface_area,2))+ "Efficency: "+str(round(ef,2)) +" cost: "+str(round(cost,2)))
print()
radius=8.10
height=11.11
cost=0.42
volume=compute_volume(radius,height)
surface_area=compute_surface_area(radius,height)
ef =efficency(volume,surface_area)
print("Can #12 Volume: "+ str(round(volume,2)) +" + surface area: "+ str(round(surface_area,2))+ "Efficency: "+str(round(ef,2)) +" cost: "+str(round(cost,2)))
