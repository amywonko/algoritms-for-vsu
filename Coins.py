import sys

try:
    number = int(input("Input your number: "))
    n = int(number)
    count = 0

    if n < 0:
        print("Error")
    else:
        while n > 0 :
            if n >= 25 :
                n = n - 25
                count = count + 1
            elif n >= 10 :
                n = n - 10
                count = count + 1
            elif n >= 5 :
                n = n - 5
                count = count + 1
            elif n >= 1 :
                n = n - 1
                count = count + 1
        print (count)

except ValueError:
        print("Number should be integer not float ")
except NameError:
    print (" ")