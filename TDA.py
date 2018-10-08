def main:
    fSp,fEp,fDistence = input("(Use the 24 house format in decimals 3:45 -> 15:45 -> 15.45 ) \n Enter your starting time: "),input("Enter your end point: "),input("Total distance traveled in km")
    fTimeTraveled = fEp - fSp
    print("The average speed was {0} km/h ".format(fTimeTraveled/fDistence))


if __name__ == '__main__':
    main()