#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
There is only one operation happening in the while loop, which tells me that this will run n amount of times.


b) O(n^c)
Because there is a nested loop, and that nested loop is multiplying the outer loop by 2 each iteration, I think this is going to run n^c times. It'll keep getting larger for each loop.


c) O(n)
This will loop and add 2 to each bunny count. If you feed it 4, it returns that there are 8 bunny ears. Simple loop, which would run n amount of times.


## Exercise II

n = max stories in building.
f = highest story an egg will break.

F is the expected return.

The best case solution would be to always drop the eggs from the 0th floor to avoid any breaking, or floors traversed. Dropping eggs from any height is a bad idea. 


``` python
# Goofy solution.
def egg_drop(n):
    f = 0
    for _ in range(len(n)): # O(n)
        f = n * 0
    return f
```
``` python
# Constant solution.
def egg_drop(n): # O(1)
    return 0
```
The goal is the devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

From a scientific standpoint, not a logical standpoint, let's create a program that checks egg breaks at each floor. At each floor we'll "drop an egg" and check if it breaks. We'll use a boolean value, recorded by the tester for whether the egg broke or not. If the egg breaks at a floor, that must be the max floor, if it survives, it must be moved up a floor and re-dropped. The formula will not actually break eggs, but should serve as a measure to find which floor it broke. We should only need 1 egg for this test, minimizing both the broken eggs, and drops at the same time.

```python
# Result recorder only returns the value of the input. This will allow us to record at each floor.
def result_recorder():
    return input("Did the egg break? T/F: ")

# Binary Search would be the best way to minimize broken eggs. Must be Log N. Recursive binary search.
# n = number of floors in building.
def egg_drop(n): 
    # We're going to drop the egg from the 0th floor, and move up the building.
    for floor in range(n): # O(n) or O(1)
        # Record the result with the helper function.
        result = result_recorder()

        # If the value is "T", the egg broke. Return floor because that is the max floor we can drop an egg from.
        if result == "T": # O(1)
            print(f"Your egg broke at floor {floor}.")
            return floor
```

```python

# Binary Search Style
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
```

