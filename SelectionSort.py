
def newArray(size=10, max=50):
    from random import randint
    return [randint(0, max) for _ in range(size)]

def selectionSort(x):
    for i in range(len(x)):
        min = i
        for j in range(min + 1, len(x)):
            if x[j] < x[min]:
                min = j
            j += 1
        if x[min] != x[i]:
            x[i], x[min] = x[min], x[i]
    return x

x = newArray()
print (x)
a = selectionSort(x)
print(a)
