import sys
range = int(input())
if range < 0 or range > 15:
    sys.exit()
vote = input()
AVotes = 0
BVotes = 0
for letter in vote:
    if letter == "A":
        AVotes += 1
    elif letter == "B":
        BVotes += 1
if AVotes > BVotes:
    print("A")
elif AVotes < BVotes:
    print("B")
elif AVotes == BVotes:
    print("Tie")