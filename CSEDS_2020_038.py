
def binary_search(arr, key):
    lo = 0
    hi = len(arr)-1

    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] < key:
            lo = mid + 1
        elif arr[mid] > key:
            hi = mid - 1
        else:
            return mid

    return -1

n = int(input("Enter length of the array: "))
arr = []
for  i in range(n):
    item = int(input("enter element of your choice: "))
    arr.append(item)

key = int(input("Enter Key what you want: "))
print(binary_search(arr, key))

