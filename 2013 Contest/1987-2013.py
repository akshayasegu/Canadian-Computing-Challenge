year = input()
notrepeat = []
while True:
    year = str(int(year)+1)
    for i in year:
        if year.count(i) > 1:
            break
        else:
            notrepeat.append(i)
            continue
    if len(notrepeat) == len(year):
        print(year)
        break
    else:
        notrepeat = []
        continue