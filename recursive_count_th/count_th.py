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
    # Break the arr into a list of individual characters
    arr = list(word)

    # If the list is empty, return 0
    if not arr:
        return 0

    # If len of arr is greater than 1
    elif len(arr) > 1:

        # If arr[0] is "t" and arr[1] is "h"
        if arr[0] == "t" and arr[1] == "h":

            # Helper
            helper(arr[0], arr[1], "Match", .5)

            # Return 1 + a re-run of this function that takes off the first letter of the arr. This will re-run until a break case, and return this final value.
            return 1 + count_th("".join(arr[1:]))
        else:

            # Helper
            helper(arr[0], arr[1], "Not", .5)

            # Return 0 + a re-run of this function that takes off the first letter of the arr. This will re-run until a break case, and return this final value.
            return 0 + count_th("".join(arr[1:]))

    # If array is less than 1, there are no more possible matches. Return 0.
    else:
        return 0
