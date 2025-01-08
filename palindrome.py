#Python Program to check given string is palindrome or not
string = input("Enter a string: ")

def is_palindrome(s):
    processed_string = ''.join(filter(str.isalnum, s)).lower()
    return processed_string == processed_string[::-1]

print(f"'{string}' is a palindrome: {is_palindrome(string1)}")
