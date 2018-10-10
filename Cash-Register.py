def main():
    sItem = {1:"apple",2:"Chips",3:"Milk",4:"Bread"}
    cashout = []

    print("Id   Item \n")

    for i in sItem:
        print(i,"  ",sItem[i])

    while True:
        iId,iAmount = int(input("Enter the item id:  ")),int(input("Enter Amount of items: "))


if __name__ == '__main__':
    main()