alpha = "aбвгдеёждзийклмнопрстуфхцчшщъьэюя"
secret = input("Введите свое сообщение:\n ")
secret = secret.lower()
key = input("Введите ключ:\n ")
key *= len(secret) // len(key) + 1

text = ''.join([chr((ord(j) + ord(key[i])) % 33 + ord('А')) for i, j in enumerate(secret)])
print('Ваше сообщение: "' + text + '"')
