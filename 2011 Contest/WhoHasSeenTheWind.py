import sys
h = int(input())
M = int(input())
A=0
for i in range(1,M+1):
    A = (-6*(i**4)) + (h*(i**3)) + (2*(i**2)) + i
    if A <= 0:
        print("The balloon first touches ground at hour:\n" + str(i))
        sys.exit()
print("The balloon does not touch ground in the given time.")