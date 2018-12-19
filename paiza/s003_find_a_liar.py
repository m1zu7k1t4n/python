# coding : utf-8

def solve(say_person, persons):
    result = 0
    if persons == 1:
        result = -1
    for (sender, dialect, opt) in say_person:
        if (sender, dialect, not opt) in say_person:
            result = -1
        if sender == dialect:
            result = -1
        if (dialect, sender, opt) in say_person:
            result = -1
        if (dialect, sender, not opt) in say_person:
            result = -1
        if not result == -1:
            result += 1
    print(result)


def main():
    all_opinion = list()
    say_person = set()
    error = False
    LIAR = False
    HONEST = True

    persons, memos = [int(x) for x in input().split(" ")]

    for i in range(memos):
        all_opinion.append(input())

    # 0,2,5の添字で必要な要素、発言元、発言先、真偽の内容を取得出来る
    for string in all_opinion:
        string = string.split(" ")
        sender = string[0]
        dialect = string[2]
        ToF = string[5]

        if ToF == "liar.":
            say_person.add((sender, dialect, LIAR))
        elif ToF == "honest":
            say_person.add((sender, dialect, HONEST))

    solve(say_person, persons)


if __name__ == '__main__':
    main()
