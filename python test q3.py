#3. write a function to check if ther given string is palindrome. str='malayam'    

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
string = "malayam"
if is_palindrome(string):
    print(f"malayam is a palindrome.")
else:
    print(f"malayam is not a palindrome.")
