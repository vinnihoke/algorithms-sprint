'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
import time


def count_th(word):
    arr = list(word)
    if not arr:
        return 0
    elif len(arr) > 1:
        if arr[0] == "t" and arr[1] == "h":
            print("ARR[0] contains", arr[0])
            print("ARR[1] contains", arr[1])
            time.sleep(.5)
            return 1 + count_th("".join(arr[1:]))
        else:
            print("ARR[0] no", arr[0])
            print("ARR[1] no", arr[1])
            time.sleep(.5)
            return 0 + count_th("".join(arr[1:]))
    else:
        return 0
