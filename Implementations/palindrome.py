
def palindrome(Str):
    
    if len(Str) <= 1: return True
    elif len(Str) > 1: 
        return Str[0] == Str[len(Str)-1] and palindrome(Str[1:-1:])

if __name__ == "__main__":
    print(palindrome("1231"))

