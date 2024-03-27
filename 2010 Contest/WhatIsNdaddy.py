import sys
n = int(input())
if (n < 1 or n > 10):
    sys.exit()
count = 0
for i in range (0,int(n/2)+1):
    if ((n-i) <= 5):
        count+= 1
print(count)
