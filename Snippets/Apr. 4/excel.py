
numbers = []
numInputs = int(input("How many Numbers? "))
for i in range(numInputs):
    num = float(input("Enter Number {}: ".format(i+1)))
    numbers.append(num)
sum = sum(numbers)
mean = sum/numInputs
print("The sum of the numbers is: ", sum)
print("The mean of the numbers is: ", mean)

    




"""

numbers = []
count = int(input("How many Numbers? "))
for i in range(count):
    number = float(input("Enter Number {}".format(i+1)))
    numbers.append(number)
total = sum(numbers)
mean = total/count

print(f"The sum of the numbers is: {total}")
print(f"The average of the numbers is: {mean}")
"""