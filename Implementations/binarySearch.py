
def binarySearch(digit, input, l, r):
    
    mid = l + (r - l) // 2
    if input[mid] == digit: return mid
    elif input[mid] > digit: return binarySearch(digit, input, l, mid-1)
    else: return binarySearch(digit, input, mid + 1, r)

if __name__ == "__main__":
    arr = [2, 3, 4, 5, 6, 7, 8, 9]
    print(binarySearch(3, arr, 0, len(arr)-1)) 

# Cannot do the method of list slicing as the index returned would be relative to the sliced array and not the original array
# This is tail recursion as the final answer is only dependant on the last recursive call alone and not those preceding it 
