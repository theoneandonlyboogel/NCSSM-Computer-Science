def binarySearch(numbers, target):
    low = 0
    high = len(numbers) -1

    while low <= high:
        mid = (low + high)//2
        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            low = mid +1
        else:
            high = mid -1
    return -1

#example usage
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 3
result = binarySearch(numbers, target)

if result != -1:
    print(f"The target number {target} is found at index {result}.")
else:
    print(f"The target number {target} is not found on this list.")