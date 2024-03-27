
def isAccending(arr):
    
    if len(arr) <= 1: return True
    return arr[len(arr)-1] >= arr[len(arr)-2] and isAccending(arr[:len(arr)-1]) 

if __name__ == "__main__":
    print(isAccending([0, 1, 4, 5, 6]))