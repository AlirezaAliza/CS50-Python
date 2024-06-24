from random import randint

while True:
    try:
        level = int(input("Level: ").strip())
        if level >= 1:
            random = randint(1, level)
            while True:
                a = int(input("Guess: ").strip())
                try:
                    if a > random:
                        print("Too large!")
                    elif a < random:
                        print("Too small!")
                    else:
                        print("Just right!")
                        break
                except (TypeError, ValueError):
                    continue
            break
    except (TypeError, ValueError):
        continue
