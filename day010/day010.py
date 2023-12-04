# check if a string is a pelidrome

def is_palindrome(s):
    cleaned_string = ''.join(s.split()).lower()
    return cleaned_string == cleaned_string[::-1]

def main():
    user_input = input("Enter a string: ")
    if is_palindrome(user_input):
        return print(f"{user_input} is a palindrome.")
    else:
        return print(f"{user_input} is not a palindrome.")


if __name__ == "__main__":
    main()