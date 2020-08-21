#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```
a) This is O(n)
    a = 1 step
    while = 1 step
    a = 1 step

    In the worst case scenario (negative integer), this requires 
    n+1 iterations to stop running. If we simplify that, it's O(n).

    2*2*2 = 8
    2*2 = 4

    -2*-2*-2 = -8
    -2*-2 = -4 + -4 + -4 = -12 (needs 3 iterations)

    -3^3 = -27
    -3^2 = -9 + -9 + -9 + -9 = -36 (needs 4 iterations)

    -4^3 = -64
    -4^2 = -16 (needs 5 iterations)
```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```
b) This is O(n). 

    If it was j += 1, it would be n steps * n steps which would be O(n^2)
    But it's not because doubling everytime makes it more like, O(n^.5(n)) or something.
    If we have O(x(n)) we simplify to n. This one looks weird but is no different I suppose.
    
    Because exponential growth goes so fast, if we had a huge dataset, those extra steps would be
    nearly negligable. So I'm sticking with O(n). If it didn't have the for loop forcing it to do 
    at least j=1 each time, it might even be O(log(n)) or something, but it has to be at least
    O(n) because of that for loop. 

c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```
c) O(1)
    This is constant because it only runs once.
    Either bunnies is zero and it returns zero,
    or it only caluclates 2+bunnyEars(bunnies-1)
    one time and returns it.

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

So, we could employ a strategy sort of like a binary search tree. We know the minimum is 1 and maximum is n.

We could test out the intial midpoint of n // 2 floor and that would tell us if we can disregard either the bottom or top half of floors. If it breaks, we need to move to the lower half. If it doesn't, we need to go to the higher half.

Then we could then change our midpoint to either the lower half or higher half and repeat this process until we
have a section of only two floors wherein one egg breaks and one does not. The one that breaks is f.

This would be O(log(n)) because we are halving the possible space with each iteration.
