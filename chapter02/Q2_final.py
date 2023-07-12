import random

while True:
    頭文字 = random.choice([chr(ord("a") + i) for i in range(26)])
    print(頭文字)
    if 頭文字 == "m":
        break
