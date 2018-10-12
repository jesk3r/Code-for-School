def main():
    sItem = {1:"apple",2:"Chips",3:"Milk",4:"Bread"}
    iItemPrice = {"apple":1.99,"Chips":2.99,"Milk":3.5,"Bread":4.99}
    cashout = []
    Numitems = []
    Totalprice = 0
    Tax = 0

    print("Id   Item \n")

    for i in sItem:
        print(i,"  ",sItem[i])

    print("\n")

    while True:
        iId,iAmount = int(input("Enter the item id:  ")),int(input("Enter Amount of items: "))

        cashout.append(iId)
        Numitems.append(float(iAmount))

        print("would you'ld you like another item ")

        respons = input().split()

        if "no" in respons:
            print("\n")
            break

    for j in range(0,len(Numitems)):
        tId = cashout[j]
        tkey = sItem[tId]


        Totalprice += iItemPrice[tkey] * Numitems[j]




    Tax += Totalprice * 0.13

    print("Items","        ","Amount","\n")

    for i in range(0,len(cashout)) :
        tId = cashout[i]
        print(sItem[tId],"        ",int(Numitems[i]))

    print("\nsubtotal: $ {0}".format(Totalprice))
    print("Total Tax: $ {0}".format(Tax))
    print("Amount due: $ {0}".format(Totalprice+Tax))

if __name__ == '__main__':
    main()