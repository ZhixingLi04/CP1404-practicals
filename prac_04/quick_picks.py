import random
NUMBERS_OF_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45
quick_pick = int(input("How many quick picks? "))
for a in range(quick_pick):
    random_number = []
    for i in range(NUMBERS_OF_LINE):
        number = int(random.randint(MIN_NUMBER,MAX_NUMBER))
        while number in random_number:
            number = int(random.randint(MIN_NUMBER,MAX_NUMBER))
        random_number.append(number)
        random_number = sorted(random_number)
    for b in range(len(random_number)):
        random_number[b] = f"{str(random_number[b]):>2}"
    print(" ".join(random_number))






