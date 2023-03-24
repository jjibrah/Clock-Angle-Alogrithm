# Give the variables needed in the test and converting  them to integers
hour = int(input("Enter the hour in 12 hour clock system\n"))
minutes = int(input("Enter the minutes\n"))

# Validating the time given by the user

if hour > 12:
    print("please enter valid hour ie(between 1-12)")
elif minutes > 60:
    print("please enter valid minutes ie(between 1-60)")
else:
    print("The time is", hour, ":", minutes)

# Calculate the difference in the angle between the hour hand and minute hand
angle = abs((((minutes / 60) + hour) * 30) - ((minutes / 60) * 360))
# Print the output
if angle == 360:
    print("The angle difference between the hour hand and the minute hand is 0")

else:
    print("The angle difference between the hour hand and the minute hand is :", angle)
