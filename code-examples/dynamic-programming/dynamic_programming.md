# Dynamic Programming

# Basic Dynamic Programming Patterns

## Caching Your Value
If you don't use recursion, you will have to "cache" your values. 

There are three primary ways to "cache" your value:
1. update a specific value again and again, this will have your answer
2. create an array, update the array, and use the last value as the answer
3. create a matrix (arrays within an array), populate the arrays, use the last square to return the answer

## Figure out the equation

# Basic Patterns Found in Leetcode

Below you will find patterns to follow for different kinds of dynamic programming problems. Below the patterns, you will find specific Leetcode problems that utilize the patterns.  

## EASY Pattern

This pattern is meant to give you a way to think about easy dynamic programming problems. It is not the most time, nor memory efficient. However, the goal here is to teach you tools that you can then iterate on. The examples also include iterations through the loops so you can see output. They are in the form of `output --> previous_output`. For instance, in `3 --> 2`, `2` was the first value it had, `3` was the second value it had.

```
    # 1. access the length of the array
    # 2. final value -- DP here: we are "caching" a value and updating it
    # 3. intermediate value
    # 4. loop 
        # 5. within loop, max or min: MAX used below 
        # 6. you'll usually have at least two of these
        # 7. start resetting for the next loop
        # -- DP below: we are repeating a mathematical equation
        #    to find out answer
        # MAX 1
        # MAX 2
```



## Easy Examples

### Easy Example: MaxSubArray

[Leetcode Link](https://leetcode.com/problems/maximum-subarray/)


```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
         # [ 1, 2, 3] array input
         # [ 1, 2] continguous subarray 
         # [ 1, 3] subarray, but not contiguous
         # 6 expected output
         # contiguous subarray sums:
         # 1, 2, 3 = 6
         # 1, 2 = 3
         # 2, 3 = 5
         
        # 1. access the length of the array
        arr_len = len(nums) # 3
        # 2. final value -- DP here: we are "caching" a value and updating it
        max_sum = nums[0] # 1 
        # 3. intermediate value
        temp_sum = nums[0] # 1
        
        # 4. loop, using range() here, but you have options
        for i in range(1, arr_len):
            num = nums[i] # 3 --> 2
            # 5. within loop, max or min: MAX below 
            # 6. you'll usually have at least two of these
            # FYI: contiguous = either the number by itself is larger
            #      or all the numbers before it PLUS the number are larger
            
            # 7. start resetting for the next loop
            #    reset the temp_sum: will change
            #    reset the max_sum: may or may not change
            
            # -- DP below: we are repeating a mathematical equation
            #.   to find out answer
            # MAX 1
            # max(3, 3 + 3 = 6) --> max(2, 1 + 2 = 3)
            temp_sum = max(num, temp_sum + num) # 6 --> 3
            # MAX 2
            # max(6, 3) --> max(1, 3)
            max_sum = max(temp_sum, max_sum) # 6 --> 3

```

### Easy Example: House Robber

[Leetcode Link](https://leetcode.com/problems/house-robber/)

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1. access the length of the array
        len_arr = len(nums) # 4
        # 2. potential final value 1
        max_val_two_houses_ago = 0
        # 3. potential final value 2
        max_val_one_house_ago = 0
                    
        # 4. loop
        for i in range(len_arr): 
            cur_house_val = nums[i] # 1 --> 3 --> 2 --> 1
​
            # 5. within loop, max or min: MAX here 
            # 6. you'll usually have at least two of these
            # -- DP below: we are repeating a mathematical equation
            #    to find out answer
            
            # 1 + 1 --> 1 + 3 --> 0 + 2 --> 0 + 1
            rob_cur_house = max_val_two_houses_ago + cur_house_val
            # 4 --> 1 --> 1 --> 0
            skip_cur_house = max_val_one_house_ago
            
            # 7. start resetting for the next loop
            max_val_two_houses_ago = max_val_one_house_ago # 4 --> 1 --> 1 --> 0
            # MAX 1
            # max(2, 4) --> max(4, 1) --> max(2, 1) --> max(1, 0)
            max_val_one_house_ago = max(rob_cur_house, skip_cur_house) # 4 --> 4 --> 2 --> 1
            
            
        # MAX 2
        # max(4, 4)
        return max(max_val_two_houses_ago, max_val_one_house_ago) # 4
```

## MEDIUM Patterns

### Pathways Pattern

This pattern is meant to give you a way to think about easy dynamic programming problems. It is not the most time, nor memory efficient. However, the goal here is to teach you tools that you can then iterate on.

```python
# cols = how many columns
# rows = how many rows

# if it doesn't already exist, create a matrix/grid
# ex. grid = [[0]* cols] * rows

# fill in the values for the first point in the grid/matrix
# ex. grid[0][0] = SOMETHING

# fill in the values for the first column
for i in range(rows):
    grid[i][0] = SOMETHING

# fill in the values for the first row
for j in range(cols):
    grid[0][j] = SOMETHING

# Starting from grid[1,1] use the numb above and left
# to fill the rest of the grid
for i in range(1,rows):
    for j in range(1,cols):
        # -- DP below: we are repeating a mathematical equation
        #    to find out answer
        grid[i][j] = SOMETHING +/- SOMETHING

# Return value stored in rightmost bottommost cell
return grid[rows-1][cols-1]
```

### Medium Pathways Example: Unique Paths I

[Leetcode Link](https://leetcode.com/problems/unique-paths/)

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # cols = how many columns
        # rows = how many rows
        # if it doesn't already exist, create a matrix/grid
        # ex. grid = [[0]* cols] * rows
        grid = [[0]*m] * n

        # fill in the values for the first point in the grid/matrix
        # NOTE: this could be left out here, but is kept to shower how the pattern is used latter
        grid[0][0] = 1

        # fill in the values for the first column
        for i in range(n):
            grid[i][0] = 1
     
        # fill in the values for the first row
        for j in range(m):
            grid[0][j] = 1

        # Starting from grid[1,1] use the numb above and left
        # to fill the rest of the grid
        for i in range(1,n):
            for j in range(1,m):
                # -- DP below: we are repeating a mathematical equation
                #    to find out answer
                grid[i][j] = grid[i-1][j] + grid[i][j-1]

        # Return value stored in rightmost bottommost cell
        return grid[n-1][m-1]
```

### Medium Pathways Example: Unique Paths II

[Leetcode Link](https://leetcode.com/problems/unique-paths-ii/)

Note: For this implementation we'll be switching values...explain how we're using 1s and 0s here

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # cols = how many columns
        # rows = how many rows
        rows = len(obstacleGrid) #
        cols = len(obstacleGrid[0])
        
        # if it doesn't already exist, create a matrix/grid --> GRID EXISTS; reuse it

        # EXTRA STEP: needed if you could start with an empty grid
        if obstacleGrid[0][0] == 1:
            return 0

        # fill in the values for the first point in the grid/matrix
        obstacleGrid[0][0] = 1

        # Filling the values for the first column
        for i in range(1,cols):
            # if previous square is 1 and current square is 0, set to 1
            # int() is an easy way to return 1 or 0 from True/False statements
            # t/4, int(true and true) = 1, int(true and false) = 0, int(false and false) = 0
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)

        # Filling the values for the first row
        for j in range(1, rows):
            # if previous square is 1 and current square is 0, set to 1
            # int() is an easy way to return 1 or 0 from True/False statements
            # t/4, int(true and true) = 1, int(true and false) = 0, int(false and false) = 0
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)

        # Starting from grid[1,1] use the numb above and left
        # to fill the rest of the grid
        for i in range(1,cols):
            for j in range(1,rows):
                # -- DP below: we are repeating a mathematical equation
                #    to find out answer
                if obstacleGrid[i][j] == 0:
                    # if current previous left square and previous right square are 0, set current square to 1
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0

        # Return value stored in rightmost bottommost cell
        return obstacleGrid[cols-1][rows-1]
```


## Dynamic Programming in Python
While many languages use recursion as the basis of dynamic programming, unfortunately, python cannot because of it's implementation. 

[Example of Recursive and Non-Recursive Python DP Solutions (and why one can't work)](https://github.com/rogue0137/practice/blob/master/leetcode_python/easy/SOLVED-maximum-subarray.py)

[Python Recursive Reading](https://realpython.com/python-thinking-recursively)