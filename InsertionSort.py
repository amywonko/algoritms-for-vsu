
def newArray(size=10, max=50):
    from random import randint
    return [randint(0, max) for _ in range(size)]


def insertionSort(x):
    for i in range(len(x)):
        j = i
        while x[j] <= x[j-1] and j > 0:
            a = x[j-1]
            x[j - 1] = x[j]
            x[j] = a
            j = j-1
    print(x)

x = newArray()
print (x)
s = insertionSort(x)
print(s)
