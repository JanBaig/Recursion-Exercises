
def printToN(N):
    if N < 1: return
    printToN(N-1)
    print(N)

if __name__ == "__main__":
    printToN(5)

    