"""
def printFib(length):  
    first = 0
    second = 1
    
    #print the intitial fib 
    print(first, second)

    #decrease length by 2
    length -= 2
    
    while length > 0:
        #printing the next number
        print(first + second)
        #update first/second
        temp = second
        second = first + second
        first = temp
        length =- 1
"""
def fibo(first, second, length):
    if length == 0:
        return
    
    print(first + second)
    #recursively call the function (updating the values)
    fibo(second, first + second, length -1)

#call that bad boy
fibo(0, 1, 100 -2)
