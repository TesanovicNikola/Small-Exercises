#Creating the palindrome test function
def TestPalindrome(text):
    #in case of entering dates, replacing the . or ,
    for char in '.,':
        text = text.replace(char, '')
    #inversing the string, if its the same, print that it is a palindrome
    if text == text[::-1]:
        print('It is a palindrome. \n')
    # inversing the string, if its not the same, print that it is not a palindrome
    if text != text[::-1]:
        print('It is NOT a palindrome. \n')
#main
if __name__ == "__main__":
    #Input left to the user to use
    k = input('Please enter the word you want checked: \n')
    inp=TestPalindrome(k)