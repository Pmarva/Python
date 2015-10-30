def main():
    algus = 100000
    lopp = 998001
    number = lopp
    numOfResult = 0
    i = 999

    while number >= algus:
        stringNumb = str(number)
        a = stringNumb[:3]
        b = stringNumb[-3:][::-1]
        if a == b:
            buffer = number
            while buffer > 1:
                while (i > 99):
                    if buffer % i == 0:
                        if numOfResult < 3:
                            buffer = buffer / i
                            numOfResult = numOfResult + 1
                            if numOfResult == 2:
                                numOfResult == 0
                                break
                        else:
                            numOfResult = 0
                            break
                    else:
                        i = i - 1
                if i <= 99:
                    i = 999
                    break
            if numOfResult == 2 and i > 99 and buffer == 1:
                return number
        number = number - 1


print(main())
