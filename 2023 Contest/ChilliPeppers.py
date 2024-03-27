N = int(input("Enter the number of chillis: "))
chilli = []
T = 0
for i in range(0,N):
    chilli.append(input("Enter the chilli name: "))
for i in chilli:
    if i == "Poblano":
        T += 1500
    elif i == "Mirasol":
        T += 6000
    elif i == "Serrano":
        T += 15500
    elif i == "Cayenne":
        T += 40000
    elif i == "Thai":
        T += 75000
    elif i == "Habenaro":
        T += 125000
print(T)