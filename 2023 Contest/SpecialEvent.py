N = int(input("Enter the Number of People Attending Your Event: "))
Days = []
for i in range (1,N+1):
    Days.append(input("Enter each person’s availability:"))
for i in range(0,N):
    Days[i] = (str(Days[i]).split(","))
