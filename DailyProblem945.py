"""
LeetCode Daily Problem 945
Minimum Increment to Make Array Unique

Goal:   You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.
        Return the minimum number of moves to make every value in nums unique.

Matthew Sienkiewich
"""

import sys
import os

def minIncrementForUnique(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    movecount = 0
    nums.sort() # Allows duplicates to be next to each other
    #print(f"array: {nums}\n")
    for i in range(1, len(nums)): # Start at index 1 so we can compare each element to the previous element
        if nums[i] <= nums[i - 1]:
            #print(f"nums[i]: {nums[i]}\nnums[i - 1]: {nums[i - 1]}\n")
            inc = nums[i - 1] - nums[i] + 1 # Find the difference and add one so nums[i] is greater by one
            #print(f"increment: {inc}\n")
            nums[i] += inc 
            movecount += inc       
    return movecount

test = [1,2,2]
test2 = [3,2,1,2,1,7]

print(f"test: {minIncrementForUnique(test)}")
print(f"test2: {minIncrementForUnique(test2)}")