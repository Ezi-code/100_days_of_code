def main():
    number = float(input("Enter number: "))
    get_number_type(number)


def get_number_type(number):
    if number != 0:
        try:
            if number % 2 == 0:
                return True
            else:
                return False
        except Exception as e:
            return e
        
if __name__ == "__main__":
    main()