def search(arr, N, x):
 
    for i in range(0, N):
        if (arr[i] == x):
            return i
    return -1
 
 
# Driver Code
if __name__ == "_main_":
    arr = [1…N]
    x = arr[x]
    N = len(arr)
 
    # Function call
    result = search(arr, N, x)
    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)

