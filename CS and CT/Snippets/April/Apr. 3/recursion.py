numbers = [45, 200, 540, 182, 1254, 904, 6932]
def findLargest(numbers):
    #if list has only 1 num, return
    if len(numbers) == 1:
        return numbers[0]
    #find largest number in the rest of the list
    else:
        largestInRest = findLargest(numbers[1:])
        #compare first number with the largest in the list
        if numbers[0] > largestInRest:
            return numbers[0]
        else:
            return largestInRest

print(findLargest(numbers))