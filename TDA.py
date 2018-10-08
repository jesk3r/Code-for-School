def main():
    fSp,fEp,fDistence = float(input("(Use the 24 house format in decimals 3:45 -> 15:45 -> 15.45 ) \nEnter your starting time: ")),float(input("Enter your end point: ")),float(input("Total distance traveled in km: "))
    fTimeTraveled = fEp - fSp
    print("The average speed was {0} km/h ".format(fDistence/fTimeTraveled))


if __name__ == '__main__':
    main()