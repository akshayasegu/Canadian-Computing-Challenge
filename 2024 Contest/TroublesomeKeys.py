
InString = input()
OutString = input()
SillyKey = ""
QuietKey = "-"
for i in range(min(len(InString), len(OutString))):
    if InString[i] == OutString[i]:
        continue
    elif InString[i] != OutString[i]:
        if QuietKey == InString[i]:
            OutString = OutString[:i]+QuietKey+OutString[i:]
        for index in range(i, len(InString)):
            if QuietKey != "-" and InString[i] != QuietKey:
                break
            if OutString[i] == InString[index]:
                QuietKey = InString[i]
                break
        if index == len(InString) - 1:
            SillyKey = InString[i] + " " + OutString[i]
    if QuietKey != "-" and SillyKey != "":
        break
if len(OutString) != len(InString) and QuietKey == "-":
    QuietKey = InString[len(InString)-1]
print(SillyKey)
print(QuietKey) 
