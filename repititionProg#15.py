while True:
    a = int(input("Enter a number: "))

    if a**2 in range(40,100):
        print("{0} squared is between 40 and 100".format(a))
        break