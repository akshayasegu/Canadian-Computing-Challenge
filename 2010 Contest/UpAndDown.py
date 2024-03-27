a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())
nicki = 0
byron = 0
def stepcalculate(a,b,nicki,s):
    nicki += (s//(a+b))*(a-b)
    if ((s%(a+b)) <= a):
        nicki += (s%(a+b))
    elif ((s%(a+b)) >= a):
        nicki += a
        nicki -= ((s%(a+b))-a)
    return nicki
    

nicki = stepcalculate(a,b,nicki,s)
byron = stepcalculate(c,d,byron,s)

if (nicki > byron) :
    print("Nikky")

elif (nicki < byron) :
    print("Byron")

elif (nicki == byron) :
    print("Tied")
