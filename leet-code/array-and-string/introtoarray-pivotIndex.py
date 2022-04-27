from typing import List

"""
	Given an array of integers `nums`,
	return the pivot index of this array.
"""

def test_pivotIndex1():
	got = pivotIndex([1,7,3,6,5,6])
	want = 3

	assert got == want

def test_pivotIndex2():
	got = pivotIndex([1,2,3])
	want = -1

	assert got == want

def test_pivotIndex3():
	got = pivotIndex([2,1,-1])
	want = 0

	assert got == want

def pivotIndex(nums: List[int]):
	# total sum of everything and initialize leftSum to 0
	total, leftSum = sum(nums), 0

	for index, value in enumerate(nums):
		# if we've found the leftmost pivot point
		if total - value == 2 * leftSum:
			# return its index
			return index

		# recalculate the leftSum
		leftSum = leftSum + value

	# default to return -1
	return -1


	# # works, but this code takes too long to run
	# for index in range(len(nums)):
	# 	if index == 0:
	# 		leftSum = 0
	# 		rightSum = sum(nums[index+1:])
	# 	elif index > 0 and index < len(nums)-1:
	# 		leftSum = sum(nums[:index])
	# 		rightSum = sum(nums[index+1:])
	# 	elif index == len(nums)-1:
	# 		leftSum = sum(nums[:index])
	# 		rightSum = 0

	# 	if leftSum == rightSum:
	# 		return index

	# return -1


if __name__ == "__main__":
	print(pivotIndex([1,7,3,6,5,6]))
	print(pivotIndex([1,2,3]))
	print(pivotIndex([2,1,-1]))

"""
LeetCode:
	Runtime: 238ms
	Memory Usage: 15.3MB
"""