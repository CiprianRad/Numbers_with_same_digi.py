# This function gets a valid input from the user


def get_natural_number():
    while True:
        try:
            n = int(input("Enter a natural number: "))
            if n > 0:
                return n
            else:
                return abs(n)
        except ValueError:
            print("Invalid input. Enter a natural number:")


def main():
    num_1 = get_natural_number()
    num_2 = get_natural_number()

    '''
    We make a set which doesn't allow values to overlap and is unindexed 
    and unordered and therefore it is best suited for our case.
    Note: Since sets are unordered, they are equal if they contain the same values.
    The rest is almost self explainatory.

    '''

    number_set_1 = set(str(num_1))
    number_set_2 = set(str(num_2))
    if number_set_1 == number_set_2:
        print("Yes, the numbers are formed using the same digits")
    else:
        print("No, they are not made using the same digits! ")


main()
