def revert(text):
    return text[::-1]

def is_palindrome(text):
    return text == revert(text)

sth = input("Eenter text:")
if is_palindrome(sth):
    print("is palindrome")
else:
    print("not palindrome")
