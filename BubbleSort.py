
def bubbleSort(List):
    for i in range (0, len(List) -1):
        for j in range(0, len(List) -1 -i):
            if List[j] > List[j+1]:
                List[j], List[j+1] = List[j+1], List[j]
    return List

List = [ 1, 20, 5, 8, 12, 16, 10]
print(bubbleSort(List))