
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [1,4,6,8]
x = 6

result = linear_search(arr, x)

if result == -1:
    print ("Element is not found")
else:
    print ("Element is found at the index %d" %(result) )
