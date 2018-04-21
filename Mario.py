
try:

    n = input("Enter Height of Pyramid: ")
    height = int(n)

    if height <= 0 or height > 23:
        print("Try again. Number should be in range from 1 to 23")
    else:
        for i in range(height):
            print(" "*(height-1*i)+("#")+("#"*(1*i)))

except ValueError:
        print("Number should be integer not float ")
except NameError:
    print (" ")