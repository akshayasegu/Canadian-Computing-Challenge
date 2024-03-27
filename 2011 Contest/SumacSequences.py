import sys
t1 = int(input())
t2 = int(input())
if (t1 > 10000 or t2 > 10000):
    sys.exit()
seq = []
seq.append(t1)
seq.append(t2)
while True:
    seq.append(seq[len(seq)-2] - seq[len(seq)-1])
    if (seq[len(seq)-1] > seq[len(seq)-2]):
        print(len(seq))
        break