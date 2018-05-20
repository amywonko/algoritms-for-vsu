#Сортировка программистов по имени
fathers = {"Rasmus Lerdorf":"php",
    "Larry Wall":"perl",
    "Brian Kernighan":"awk",
    "James Gosling":"java",
    "Simon Cozens":"parrot",
    "Guido van Rossum":"python"}

x = sorted(fathers.keys())
for language in x:
    print(language," - ",fathers[language])

#Поиск языка программирования по создателю

search = input("What's name do you want to find ?")
for key, value in fathers.items():
    if key == search:
        print(fathers[key])
    else:
        print("False")
