allTests = """
1: Age Test; using if statements
2: Counting; using while loops
3: I Increments; using for loops
4: Celsius to Fahrenheit; using conditionals and formulas"""
userStatement = int(input(f"{allTests}\n\nInput a number from 1 - 4, each one being a different demonstration of python features. "))
if userStatement == 1:
    """if statements allow us to execute certain
    pieces of code based on conditions"""
    try:
        age = int(input("Enter your age: "))
        if age < 18:
            print("You are a minor.")
        else:
            print("You are an adult.")
    except(EOFError):
        exit()
    except(KeyError, ValueError, TypeError):
        print("Bad input, you probably inputed a word instead of a number.")

elif userStatement == 2:

    #testing while statements
    count = 1
    while count < 100:
        print(count)
        count += 1
        
elif userStatement == 3:
    #very simple for loop demonstration
    for i in range(5):
        print(i)

elif userStatement == 4:
    #testing out conditionals and formulas
    print("Fahrenheit to Celsius Converter\nInput 1 for Celsius to Fahrenheit.\nInput 2 for Fahrenheit to Celsius.")
    type = int(input("    "))
    if type == 1:
        temp1 = int(input("Celsius: "))
        print(f"{temp1}°C ----> {round((temp1*1.8)+32)}°F")

    elif type == 2:
        temp2 = int(input("Fahrenheit: "))
        print(f"{temp2}°F ----> {round((temp2-32)*5/9)}°C")

elif userStatement == 9:
    first = input("First Name: ")
    last = input("Last Name: ")
    print(first+last)