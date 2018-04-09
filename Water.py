x = int(input('How many minutes do you plan to take a shower? '))

def counting_water(x):
    result = []
    if x > 0:
        result.append(x * 12)
        return result
    else:
        return print('False')

print('To do this you will need',counting_water(x),'bottles')
