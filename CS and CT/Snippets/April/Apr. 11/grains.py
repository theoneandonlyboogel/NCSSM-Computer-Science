def calculateGrain(square):
    return 2 ** (square-1)

def totalGrains(numSquares):
    total = 0
    for square in range(1, numSquares+1):
        grains = calculateGrain(square)
        total += grains
        print(f"Square {square}: {grains} grains")
    return total

numSquares = 10
total = totalGrains(numSquares)
print(f"The total amount of grains is {total} ")