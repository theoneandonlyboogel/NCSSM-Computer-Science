fibs = []
def fibo(first, second, length):
    if length == 0:
        return
    
    third = first+second
    print(third)
    fibs.append(third)
    #recursively call the function (updating the values)
    fibo(second, first + second, length -1)
i = int(input("How many sequences? "))
sequenceTF = bool(input("Do you want a specific sequence? Press enter for No, any key and enter for yes. "))

if sequenceTF == True:
    sequenceNum = int(input("Which sequence do you want? "))
fibo(0, 1, i)
if bool(sequenceNum) == True:
    print(f"-----------------------------------------\n{fibs[sequenceNum-1]}")
