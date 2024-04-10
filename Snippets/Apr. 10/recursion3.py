#for loop to press button 5 times (1st task)
for i in range(5):
    print("Pressing the button... Press", i +1)
print("Challenge 1 Completed!")

#recursive loop for checking big and small gears (2nd task)
gears = [5, 2, 8, 1, 9, 3, 6, 4, 7]
smallGears = []
largeGears = []
for gear in gears:
    if gear < 5:
        smallGears.append(gear)
        print(f"Gear size {gear} added to the small pile")
    else:
        largeGears.append(gear)
        print(f"Gear size {gear} added to the large pile")

print(f"Small gears: {smallGears}")
print(f"Large gears: {largeGears}")
print("Challenge 2 Completed!")

#rotating levers(?) 90 degrees clockwise (3rd and final task)
for i in range(3):
    print("Rotating the levers 90 degrees clockwise... Rotation", i +1)
print("Challenge 3 Completed!")