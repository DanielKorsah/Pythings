def palindrome(results, x, y):
    z = str(x * y)
    z_back = z[::-1]
    if z == z_back:
        results.append(int(z))
    return results;

answers = []
largest = 0
for i in range(101, 1000):
    for j in range(101, 1000):
        answers = palindrome(answers, i, j)
for i in range(len(answers)):
    if largest < answers[i]:
        largest = answers[i]
print(largest)



