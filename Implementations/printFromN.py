
def printFromN(N):
    if N < 1: return
    print(N)
    printFromN(N-1)

if __name__== "__main__":
    printFromN(5) 
