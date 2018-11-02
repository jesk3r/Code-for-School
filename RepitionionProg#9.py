iTerms = 3
iXvalue = 2


def sumofNumbers(terms,x):
    iTotal = 0

    if terms  < 1:
        return x
    else:
        iTotal += sumofNumbers(terms-1,x)

        return x**terms


print(sumofNumbers(iTerms+1,iXvalue))

