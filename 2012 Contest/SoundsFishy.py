depth1 = int(input())
depth2 = int(input())
depth3 = int(input())
depth4 = int(input())
if (depth4 > depth3 > depth2 > depth1):
    print("Fish Rising")
elif (depth4 < depth3 < depth2 < depth1):
    print("Fish Diving")
elif (depth4 == depth3 == depth2 == depth1):
    print("Fish At Constant Depth")
else:
    print("No Fish")