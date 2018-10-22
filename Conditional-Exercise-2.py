def main():
    for i in range(0,10):
        fWeight = float(input("Enter weight in kg: "))

        if fWeight >80:
            print("The category they belong to would be: Heavy weight\n")
        elif fWeight>60 and fWeight<80:
            print("The category they belong to would be: Medium wight\n ")
        else:
            print("The category they belong to would be: Light wight\n ")


if __name__ == '__main__':
    main()