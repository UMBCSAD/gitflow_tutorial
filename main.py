def isEven(num):
    if num == 0: 
        return True
    elif num == 1:
        return False;
    elif num == 2:
        return True
    elif num == 3:
        return False
    elif num == 4:
        return True
    else:
        print("Not implemented")
        return False

def main():
    print("Are these numbers even?")

    lst = [2,4,6,7,9]
    for l in lst:
        print(isEven(l))


main()
