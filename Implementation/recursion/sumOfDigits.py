
def sumOfDigits(N):
    if N//10 <= 0: return N
    return N%10 + sumOfDigits(N//10)

if __name__ == "__main__":
    print(sumOfDigits(123)) # 1 + 2 + 3