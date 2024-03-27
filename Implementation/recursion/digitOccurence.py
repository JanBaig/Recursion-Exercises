
def digitOccurence(digit, input):

    if input//10 <= 0 and input%10 == digit: return 1
    elif input//10 <= 0: return 0
    
    if (input%10) == digit: return 1 + digitOccurence(digit, input//10)
    else: return digitOccurence(digit, input//10)   

if __name__ == "__main__":
    print(digitOccurence(6, 6709090)) 

