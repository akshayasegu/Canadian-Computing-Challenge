K = int(input())
initialword = input()
finalword = ""
i = 1
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for letter in initialword:
    letterindex = alphabet.index(letter) - ((3*i) + K)
    while letterindex < 0:
        letterindex = 26+letterindex
    finalword+=(alphabet[letterindex])
    i+=1
print(finalword)
