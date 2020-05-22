def egg_drop(n):
    # The lowest floor would be 0
    low = 0
    # The highest floor would be n
    high = n

    #  If low is less than or equat to high
    while low <= high:
        #  Split the floors in half.
        mid = (low + high) // 2

        # The guess would be the middle.
        guess = mid

        # If the middle is the lowest
        if guess == low:
            return mid
        # If the guess is greater than Low
        if guess > low:
            high = mid - 1
        # If the low is less
        else:
            low = mid + 1
    return low


print(egg_drop(5))
