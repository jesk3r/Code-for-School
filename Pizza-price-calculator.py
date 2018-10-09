def main():
    iNumberofPizzas = int(input("Enter the number of pizzas: "))
    fPriceofPizza = 5.99

    print("price without tax ${0}".format(iNumberofPizzas * fPriceofPizza))

    fTax = (iNumberofPizzas * fPriceofPizza) * 0.13

    print("price with tax ${0}".format(iNumberofPizzas * fPriceofPizza + fTax))

if __name__ == '__main__':
    main()