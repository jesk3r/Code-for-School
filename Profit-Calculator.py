def main():
    fExpenses,fRevenue = float(input("Enter the expense: $ ")), float(input("Enter the Revenue: $ "))

    print("${0}".format(fRevenue - fExpenses))

if __name__ == '__main__':
    main()