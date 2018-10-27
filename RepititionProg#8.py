print("what would you like to count down to: 5,50 or would you like to enter your own number  ")
sResponds = input("Enter value: ")

iCounter = 100

print(sResponds)
if sResponds == "5":
    while 5 <= iCounter:
        print(iCounter-5)
        iCounter -= 5

elif sResponds == "50":
    while 50 <= iCounter:
        print(iCounter-5)
        iCounter -= 5
else:
    while int(sResponds) <= iCounter:
        print(iCounter-5)
        iCounter -= 5
