def main():
    fMark,fTotalMark = float(input("Enter the mark you got: ")), float(input("Enter the total number of marks possible: "))

    print("{0}%".format((fMark/fTotalMark)*100))



if __name__ == '__main__':
    main()