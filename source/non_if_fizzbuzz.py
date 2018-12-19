def fizzbuzz(data):
    for index in range(15):
        _ = data[index]
    print("fizzbuzz")


def fizz(data):
    for index in range(3):
        _ = data[index]
    print("fizz")


def buzz(data):
    for index in range(5):
        _ = data[index]
    print("buzz")


def other(data):
    print(len(data))


max_num = int(input())
for i in range(max_num + 1):
    sample = [0 for x in range(1, i + 1)]
    try:
        data = [sample[x:x + 15] for x in range(0, i, 15)]
        fizzbuzz(data[-1])
    except:
        try:
            data = [sample[x:x + 3] for x in range(0, i, 3)]
            fizz(data[-1])
        except:
            try:
                data = [sample[x:x + 5] for x in range(0, i, 5)]
                buzz(data[-1])
            except:
                other(sample)
