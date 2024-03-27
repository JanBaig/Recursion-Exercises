
# What is a way that we can return an array list with answers from the individual function calls
# WITHOUT passing the return array as a function parameter? 

def linearSearchModified(arr, target, index):
    
    newList = []

    if index == len(arr)-1: return newList

    # the list is updated for an individual function call only
    if arr[index] == target: newList.append(index) 

    returnList = linearSearchModified(arr, target, index + 1)

    for i in returnList:
        newList.append(i)

    return newList 

if __name__ == "__main__":
    print(linearSearchModified([3, 4, 77, 12, 56, 12, 6], 12, 0)) 