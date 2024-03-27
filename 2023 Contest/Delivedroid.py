P = int(input("Enter the number of packages delivered: "))
C = int(input("Enter the number of collisions made: "))
F = 50*P - 10*C
if P > C :
    F += 500
print(str(F))