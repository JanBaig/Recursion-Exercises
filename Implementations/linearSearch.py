
def linearSearch(arr, target):
    
    if len(arr) == 1 and arr[0] != target: return False
    elif arr[len(arr)-1] == target: return True 
    else: return linearSearch(arr[:len(arr)-1], target)  

if __name__ == "__main__":
    print(linearSearch([1, 3, 5, 6, 8], 100))
