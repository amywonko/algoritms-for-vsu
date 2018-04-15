
def search(list,num, first, last):
    if last<first:
        return False

    else:
        mid = (last + first) // 2
        if num == list[mid]:
            return mid
        elif num < list[mid]:
            return search(list,num,first, mid - 1)
        else:
            return search(list, num, mid + 1, last)


list = [1, 2, 4, 8, 10, 15, 18, 25, 32]

num = 14
first = 0
last = len(list)

x = search(list,num, first, last)
if x == False:
    print("Sorry", num, "not here")
else:
    print("Your", num, "is", x)

