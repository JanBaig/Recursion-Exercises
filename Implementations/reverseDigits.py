
def reverseDigits(N):
    if N//10 <= 0: return str(N) 
    return str(N%10) + reverseDigits(N//10) 

if __name__ == "__main__":
    print(reverseDigits(1234))