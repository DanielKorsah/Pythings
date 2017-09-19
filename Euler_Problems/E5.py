def div(j):
    correct = True
    for i in range(1, 21):
        if j % i != 0:
            correct = False
            break
    return correct


i = 20
while True:
   # print(i)
    if div(i) == True:
        print(i)
        break
    i += 20
