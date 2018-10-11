def main():
    sItem = {1:"apple",2:"Chips",3:"Milk",4:"Bread"}
    iItemPrice = {"apple":1.99,"Chips"}
    cashout = []
    Numitems = []

    print("Id   Item \n")

    for i in sItem:
        print(i,"  ",sItem[i])

    print("\n")

    while True:
        iId,iAmount = int(input("Enter the item id:  ")),int(input("Enter Amount of items: "))

        cashout.append(iId)
        Numitems.append(iAmount)

        print("would you'ld you like another item ")

        respons = input().split()

        if "no" in respons:
            break



def receipt(cout,numi):
    totalprice = 0
    try:
        for




if __name__ == '__main__':
    main()