try:
    while True:
        number = int(input().strip())
        num = number.split()
        num = [int(i) for i in num]
        for first in range(3):
            first += 1
except EOFError:
    pass
