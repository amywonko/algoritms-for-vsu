alpha = "aбвгдеёждзийклмнопрстуфхцчшщъьэюя"
secret = input("Введите свое сообщение: ")
secret = secret.lower()
text = ""
key = int(input("Введите сдвиг от 2-х до 32-х:\n "))
def cypher(input, key):
    if key > 32:
        key = 32
    elif key < 2:
        key = 2

for i in secret:
    text+= alpha[(alpha.index(i) + key) % len(alpha)]
print('Ваше сообщение: "' + text + '"')