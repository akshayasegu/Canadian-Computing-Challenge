import sys
angle1 = int(input())
angle2 = int(input())
angle3 = int(input())
if angle1 < 0 or angle1 > 180:
    sys.exit()
if angle2 < 0 or angle2 > 180:
    sys.exit()
if angle3 < 0 or angle3 > 180:
    sys.exit()
if angle1 == 60 and angle2 == 60 and angle3 == 60:
    print("Equilateral")
elif angle1 + angle2 + angle3 > 180:
    print("Error")
elif angle1 == angle2 or angle2 == angle3 or angle1 == angle3:
    print("Isosceles")
elif angle1 != angle2 or angle2 != angle3 or angle1 != angle3:
    print("Scalene")