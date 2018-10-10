def main():
    sItem = {1:"apple",2:"Chips",3:"Milk",4:"Bread"}
    cashout = []
    Numitems = []

    print("Id   Item \n")

    for i in sItem:
        print(i,"  ",sItem[i])

    while True:
        iId,iAmount = int(input("Enter the item id:  ")),int(input("Enter Amount of items: "))

        cashout.append(iId)
        Numitems.append(iAmount)

        print("would you'ld you like another item \n")

        respons = input().split()

        if "yes" in respons:
            continue
        elif "no" in respons:
            break

if __name__ == '__main__':
    main()