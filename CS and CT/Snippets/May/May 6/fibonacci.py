"""
#iterative with for loop
def printFib(length):
    first = 0
    second = 1

    print(first, second, sep="+")
    for i in range(2, length):
        temp = second
        second = first + second
        first = temp
        print(second)
        i+=2
print("Fib Series")
printFib(20)
"""
"""
#Mr. Robinson's approach
def fibonacci(n):
    if n <= 1:
        return n
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
            return fib[n]
n = int(input("Enter the value of n: "))
print("The nth number in the sequence is: {fibonacci(n)})
"""
fibs = []
#recursive version, with challenge
def fibo(first, second, length):
    if length == 0:
        return
    
    #third is effectively a temp var
    third = first+second
    print(third)
    fibs.append(third)
    #recursively call the function (updating the values)
    fibo(second, first + second, length -1)

#asking for how many sequences
i = int(input("How many sequences? "))
#True False if you want a specific sequence at the end
sequenceTF = bool(input("Do you want a specific sequence? Press enter for No, any key for yes. "))
#if sequenceTF is true, aka they inputed anything, ask for which sequence they want. Else, just print as normal.
if sequenceTF == True:
    sequenceNum = int(input("Which sequence do you want? "))
fibo(0, 1, i)
if bool(sequenceNum) == True:
    print(f"Specific sequence:\n{fibs[sequenceNum-1]}")