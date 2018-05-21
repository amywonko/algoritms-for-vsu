alpha = "aбвгдеёждзийклмнопрстуфхцчшщъьэюя"
secret = input("Введите свое сообщение:\n ")
secret = secret.lower()
text = ""
key = input("Введите ключ:\n ")
k = len(key)

for i in secret:
    text+= alpha[(alpha.index(i) + k) % len(alpha)]
print('Ваше сообщение: "' + text + '"')