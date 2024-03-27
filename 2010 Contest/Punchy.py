A = 0
B = 0

while True:
    instruct = input()
    if "7" in instruct:
        break
    elif "1" in instruct:
        if (instruct[2] == 'A'):
            A = int(instruct[4])
        elif (instruct[2] == 'B'):
            B = int(instruct[4])
    elif "2" in instruct:
        if (instruct[2] == 'A'):
            print(A)
        elif (instruct[2] == 'B'):
            print(B)
    elif "3" in instruct:
        if (instruct[2] == 'A'):
            if (instruct[4] == 'B'):
                A += B
            elif (instruct[4] == 'A'):
                A += A
        elif (instruct[2] == 'B'):
            if (instruct[4] == 'B'):
                B += B
            elif (instruct[4] == 'A'):
                B += A
    elif "4" in instruct:
        if (instruct[2] == 'A'):
            if (instruct[4] == 'B'):
                A = A * B
            elif (instruct[4] == 'A'):
                A = A * A
        elif (instruct[2] == 'B'):
            if (instruct[4] == 'B'):
                B = B * B
            elif (instruct[4] == 'A'):
                B = A * B
    elif "5" in instruct:
        if (instruct[2] == 'A'):
            if (instruct[4] == 'B'):
                A = A - B
            elif (instruct[4] == 'A'):
                A = A - A
        elif (instruct[2] == 'B'):
            if (instruct[4] == 'B'):
                B = B - B
            elif (instruct[4] == 'A'):
                B = A - B
    elif "6" in instruct:
        if (instruct[2] == 'A'):
            if (instruct[4] == 'B'):
                A = A // B
            elif (instruct[4] == 'A'):
                A = A // A
        elif (instruct[2] == 'B'):
            if (instruct[4] == 'B'):
                B = B // B
            elif (instruct[4] == 'A'):
                B = A // B