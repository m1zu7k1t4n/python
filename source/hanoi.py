def move(a, b, c, n):
    """
    A,B,C Pole and number Board
    """
    global count
    if(n == 1):
        print("{}->{}".format(a, b))
        count += 1
    else:
        move(a, c, b, n - 1)
        print("{}->{}".format(a, b))
        count += 1
        move(c, b, a, n - 1)

n = 4
count = 0
move('A', 'B', 'C', n)
print(count)
