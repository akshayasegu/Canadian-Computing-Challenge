import sys
RoundNum = int(input())
Antonia = 100
David = 100
if int(RoundNum) < 1 or int(RoundNum) > 15:
    sys.exit()
for i in range (RoundNum):
    Score = input()
    if int(Score[0]) < 1 or int(Score[0]) > 6 or int(Score[2]) < 1 or int(Score[2]) > 6:
        sys.exit()
    if int(Score[0]) < int(Score[2]):
        Antonia -= int(Score[2])
    elif int(Score[0]) > int(Score[2]):
        David -= int(Score[0])
print(Antonia)
print(David)