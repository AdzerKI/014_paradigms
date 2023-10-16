number = 5

def tableCount(n):
    for i in range(1, n):
        for j in range(1, 10):
            print(i, "*", j, "=", i * j, "\n")

tableCount(number)