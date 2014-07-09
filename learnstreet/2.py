#string defs project
def revers(str):
    # Accept an input string, str, and reverse its characters in order
    "REPLACE THIS CODE WITH YOUR CONVERSION METHOD"
    return str[::-1]

def uppercase(str):
    # Convert all the characters of the input string, str, to upper
    # case. Reurn the uppercased string.
    "REPLACE THIS CODE WITH YOUR CONVERSION METHOD"
    return str.upper()

def palindrome(str):
    # Check if the input string, str, is spelled the same forwards
    # as it is spelled backwards.
    # Return "is a palindrome" if it is, or "is not a palindrome" if it is not.
    "REPLACE THIS CODE WITH YOUR CONVERSION METHOD"
    ll = len(str)
    middle = ll/2
    if ll%2 == 0:
        first = str[0:middle]
        last = str[middle:]
        if first == revers(last):
            print "is a palindrome"
        else:
            print "is not a palindrome"
    else:
        first = str[0:middle]
        last = str[middle+1:]
        if first == revers(last):
            print "is a palindrome"
        else: 
            print "is not a palindrome"

def main():
    string = raw_input("put a word here : ")
    palindrome(string)

if __name__ == "__main__":
    main()