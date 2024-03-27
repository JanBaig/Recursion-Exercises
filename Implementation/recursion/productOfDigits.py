
def productOfDigits(N):
    if N//10 <= 0: return N
    return (N%10) * productOfDigits(N//10)

if __name__ == "__main__":
    print(productOfDigits(203))