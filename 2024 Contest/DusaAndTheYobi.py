D = int(input()) #Dusa Size
while True:
    Y = int(input()) #Yobi Size
    if ((D-Y) > 0):
        D += Y
        continue
    else:
        print(D)
        break