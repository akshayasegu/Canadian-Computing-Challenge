import sys
boringseq = [[0,-1],[0,-2],[0,-3],[1,-3],[2,-3],[3,-3],[3,-4],[3,-5],[4,-5],[5,-5],[5,-4],[5,-3],[6,-3],[7,-3],[7,-4],[7,-5],[7,-6],[7,-7],[6,-7],[5,-7],[4,-7],[3,-7],[2,-7],[1,-7],[0,-7],[-1,7],[-1,6],[-1,5]]
i = len(boringseq)-1
l = i
com = input()
def checkfunct(com):
    if "q" in com:
        return False
    elif "l" in com:
        if ([boringseq[l][0] - int(com[2]),boringseq[l][1]] not in boringseq):
            boringseq.append([boringseq[l][0] - int(com[2]),boringseq[l][1]])
    elif "r" in com:
        if ([boringseq[l][0] + int(com[2]),boringseq[l][1]] not in boringseq):
            boringseq.append([boringseq[l][0] - int(com[2]),boringseq[l][1]])
    elif "u" in com:
        if ([boringseq[l][0],boringseq[l][1] + int(com[2])] not in boringseq):
            boringseq.append([boringseq[l][0] - int(com[2]),boringseq[l][1]])
    elif "d" in com:
        if ([boringseq[l][0],boringseq[l][1] - int(com[2])] not in boringseq):
            boringseq.append([boringseq[l][0] - int(com[2]),boringseq[l][1]])
    if (boringseq.count(boringseq[l+1]) != 1):
       return False
    elif (boringseq.count(boringseq[l+1]) == 1):
        return True
while True:
    if (checkfunct(com) == True):
        print (boringseq[l])
        com = input("1")
        l+=1
        continue
    else:
        for i in range (i,l+1):
            if (boringseq.count(boringseq[i+1]) != 1):
                print (boringseq[i][0] + " " + boringseq[i][1] + " DANGER")
                sys.exit
            elif (boringseq.count(boringseq[i+1]) == 1):
                print (boringseq[i][0] + " " + boringseq[i][1] + " safe")
""" while True:
    com = input()
    if "q" in com:
        sys.exit()
    elif "l" in com:
        if ([boringseq[i][0] - int(com[2]),boringseq[i][1]] not in boringseq):
            boringseq.append([boringseq[i][0] - int(com[2]),boringseq[i][1]])
    elif "r" in com:
        if ([boringseq[i][0] + int(com[2]),boringseq[i][1]] not in boringseq):
            boringseq.append([boringseq[i][0] - int(com[2]),boringseq[i][1]])
    elif "u" in com:
        if ([boringseq[i][0],boringseq[i][1] + int(com[2])] not in boringseq):
            boringseq.append([boringseq[i][0] - int(com[2]),boringseq[i][1]])
    elif "d" in com:
        if ([boringseq[i][0],boringseq[i][1] - int(com[2])] not in boringseq):
            boringseq.append([boringseq[i][0] - int(com[2]),boringseq[i][1]])
    if (boringseq.count(boringseq[i+1]) != 1):
        print (boringseq[i][0] + " " + boringseq[i][1] + " DANGER")
        sys.exit()
    elif (boringseq.count(boringseq[i+1]) == 1):
        print (boringseq[i][0] + " " + boringseq[i][1] + " safe")
    i+=1 """