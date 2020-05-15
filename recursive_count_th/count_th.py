'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
import time


def helper(idx1, idx2, message, sleep):
    print(f"{message}", idx1)
    print(f"{message}", idx2)
    time.sleep(sleep)


def count_th(word):
    arr = list(word)
    if not arr:
        return 0
    elif len(arr) > 1:
        if arr[0] == "t" and arr[1] == "h":
            helper(arr[0], arr[1], "Match", .5)
            return 1 + count_th("".join(arr[1:]))
        else:
            helper(arr[0], arr[1], "Not", .5)
            return 0 + count_th("".join(arr[1:]))
    else:
        return 0
