import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    lst = input()
    card = {"S": 13, "D": 13, "H": 13, "C": 13}
    err = 0

    for i in range(0, len(lst), 3):
        if lst.count(lst[i:i+3]) > 1:
            card = {"ERROR": "ERROR"}
            break
        card[lst[i]] -= 1

    print(f"#{test_case}", *card.values())










