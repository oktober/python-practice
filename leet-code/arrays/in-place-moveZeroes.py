from typing import List

"""
	Given an array of integers,
	move all 0's to the end of it
	while maintaining the relative order of the non-zero elements.
	Return the original array.
"""

def test_moveZeroes1():
	got = moveZeroes([0,1,0,3,12])
	want = [1,3,12,0,0]

	assert got == want

def test_moveZeroes2():
	got = moveZeroes([0])
	want = [0]

	assert got == want

def test_moveZeroes2():
	got = moveZeroes([1,0,1])
	want = [1,1,0]

	assert got == want

def moveZeroes(nums: List[int]):
    # set the zeroIndex to the first index of array
    zeroIndex = 0

    # loop over the array
    for index in range(len(nums)):
        # if this element is not a zero
        if nums[index] != 0:
            # swap it with the element at zeroIndex
            nums[index], nums[zeroIndex] = nums[zeroIndex], nums[index]
            # increment the zeroIndex
            zeroIndex += 1

	return nums

if __name__ == "__main__":
	print(moveZeroes([0,1,0,3,12]))
	print(moveZeroes([0]))
	print(moveZeroes([1,0,1]))

"""
LeetCode:
	Runtime: 255ms
	Memory Usage: 15.6MB
"""