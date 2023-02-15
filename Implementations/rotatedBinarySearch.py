

def rotatedBS(arr, target, start, end):
    
    if (start > end): return -1

    mid = start + (end - start) // 2
    
    if (arr[mid] == target): return mid

    if (arr[start] < arr[mid]): # the first half of the array is sorted - check if num lies here
        if ( target >= arr[start] and target <= arr[end]): return rotatedBS(arr, target, start, mid-1)
        else: return rotatedBS(arr, target, mid + 1, end)

    if target >= arr[mid] and target <= arr[end]: return rotatedBS(arr, target, mid + 1, end)
    
    else: return rotatedBS(arr, target, start, mid - 1) 
    
if __name__ == "__main__":
    rotatedBS()
