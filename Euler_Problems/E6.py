
sumSquares = 0
total = 0
for i in range(1,101):
    total += i
    square = i * i
    sumSquares += square
totalSquared = total * total
print(totalSquared - sumSquares)
