sortList = [1, 5, 4, 3, 7, 3, 25]

# Императивный
def sort_list_imperative(a):
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

print(sort_list_imperative(sortList))


# Декларативный
print(sorted(sortList))
