while True:
    grade = input("What's the grade percentage? ").strip("%").strip("0.")
    try:
        grade = int(grade)

        if grade >= 90:
            print("A")
        elif grade >= 80 and grade < 90:
            print("B")
        elif grade >= 70 and grade < 80:
            print("C")
        elif grade >= 60 and grade < 70:
            print("D")
        else:
            print("F")
    except(ValueError):
        print("Incorrect notation. Input as --%")
    input("Do you want to continue? Type done or press Ctrl + D to exit. ").lower()
    if input == "done" or EOFError:
        exit()
