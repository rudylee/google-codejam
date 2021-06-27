a = [1,2,3,4,5]

def binary_search(target, left, right):
    while left <= right:
        mid = (left + right) // 2

        if a[mid] == target:
            return mid

        if a[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

print(binary_search(1, 0, len(a) - 1))
