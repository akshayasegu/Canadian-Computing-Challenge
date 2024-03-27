speedlimit = int(input("Enter the speed limit: "))
carspeed = int(input("Enter the recorded speed of the car: "))
if (carspeed <= speedlimit):
    print("Congratulations, you are within the speed limit!")
elif (carspeed - speedlimit <= 20):
    print("You are speeding and your fine is $100.")
elif (carspeed - speedlimit <= 30):
    print("You are speeding and your fine is $270.")
elif (carspeed - speedlimit >= 31):
    print("You are speeding and your fine is $500.")