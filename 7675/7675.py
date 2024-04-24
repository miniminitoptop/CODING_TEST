import sys
<<<<<<< HEAD
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range (1, T+1):
    N = int(input())

    in_str = input().replace('!', '.').replace('?','.')
    lst1 = list(in_str.split("."))

    lst = [i for i in lst1 if i != ""]

    print(lst)

    ans_lst = [0 for i in range(N)]

    for i in range(len(lst)):
        lst[i] = lst[i].split()

        for j in range(len(lst[i])):
            if "A" <= lst[i][j][0] <= "Z":
                no = 0
                for k in range(1, len(lst[i][j])):
                    if not "a" <= lst[i][j][k] <= "z":
                        no = 1
                        break
                if no == 1:
                    continue
                ans_lst[i] += 1

    print(f'#{test_case} {" ".join(list(map(str,ans_lst)))}')

=======
sys.stdin = open("input.txt","r")
def chk_name(word):
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    points = '.?!'

    if word[0] not in upper:
        return False
    if word[0] in upper and len(word) == 1:
        return True
    for i in range(1, len(word) - 1):
        if word[i] not in lower:
            return False
    if word[-1] not in lower and word[-1] not in points:
        return False
    return True


def chk_sentence(word):
    points = '.?!'
    if word[-1] in points:
        return True
    return False


T = int(input())

for TC in range(1, T + 1):
    N = int(input())
    words = []
    answer = 0
    s = ''
    while (s.count('.') + s.count('?') + s.count('!') < N):
        words += input().split()
        s = ''.join(words)

    print(f"#{TC}", end=' ')
    for word in words:
        if chk_name(word) is True:
            # print(f"{word} is word")
            answer += 1
        if chk_sentence(word) is True:
            # print(f"{word} is end of sentence")
            print(answer, end=' ')
            answer = 0
    print()
>>>>>>> 860fbe1cff9466011cf1882927516a9984751cae
