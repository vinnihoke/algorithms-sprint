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

The best case solution would be to always drop the eggs from the 0th floor to avoid any breaking. Dropping eggs from any height is a bad idea. 

```
def egg_drop(n):
    f = 0
    for _ in range(len(n)): # O(n)
        f = n * 0
    return f
```
```
def egg_drop(n): # O(1)
    return 0
```

From a scientific standpoint, not a logical standpoint, let's create a program that checks egg breaks at each floor. At each floor we'll "drop an egg" and check if it breaks. We'll use a boolean value, recorded by the tester for whether the egg broke or not. If the egg breaks at a floor, that must be the max floor, if it survives, it must be moved up a floor and re-dropped. The formula will not actually break eggs, but should serve as a measure to find which floor it broke.

```python
# Result recorder only returns the value of the input. This will allow us to record at each floor.
def result_recorder():
    return input("Did the egg break? T/F: ")

# n = number of floors in building.
def egg_drop(n): 
    # We're going to drop the egg from the 0th floor, and move up the building.
    for floor in n: # O(n)
        # Record the result with the helper function.
        result = result_recorder()

        # If the value is "T", the egg broke. Return floor because that is the max floor we can drop an egg from.
        if result == "T":
            return floor
```
        

