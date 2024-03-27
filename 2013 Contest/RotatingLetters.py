import sys
string = input()
string = string.upper()
rotatableletters = ["I","O","S","H","Z","X","N"]
if len(string) > 30:
    sys.exit()
for i in range (len(string)):
    if string[i] in rotatableletters:
        continue
    else:
        print("NO")
        sys.exit()
print("YES")