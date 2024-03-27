
def sumNToOne(N):
    if N == 1: return 1
    return N + sumNToOne(N-1)

if __name__ == "__main__":
    print(sumNToOne(4)) 