import sys
N = int(input())
Scores = []
for i in range (N):
    s = int(input())
    if s < 0 or s > 75:
        sys.exit()
    Scores.append(s)
def findlargest(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
    return max
def removehighest(Scores, NonGold):
    highest = findlargest(Scores)
    for score in Scores:
        if score != highest:
            NonGold.append(score)
        else:
            continue
    Scores = NonGold
    return Scores

NonGold = []
Scores = removehighest(Scores, NonGold)
NonSilver = []
Scores = removehighest(Scores, NonSilver)
Bronze = []
highest = findlargest(Scores)
for score in Scores:
    if score == highest:
        Bronze.append(score)
    else:
        continue
print(str(Bronze[0]) + " " + str(len(Bronze)))