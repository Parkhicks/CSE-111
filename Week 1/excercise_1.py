data = []
data.append([5,4,3,2,0.4807692307692308])
data.append([9,1,4,6,1.5576923076923077])

def compute_data(a,b,c,d):
    return (int(a)/int(b))*(int(a)/((int(c)**2) + (int(d)**2)))

for test in data:
    print(compute_data(test[0], test[1], test[2], test[3])== test [4])