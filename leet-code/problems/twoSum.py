from typing import List

"""
	Given an array of integers `nums` and an integer `target`,
	return the indices of the two values
	that add up to `target`.
	Assume there's only one solution.
	Don't use the same element twice.
"""

def test_twoSum1():
	got = twoSum([2,7,11,15], 9)
	want = (0,1)

	assert got == want

def test_twoSum2():
	got = twoSum([3,2,4],6)
	want = (1,2)

	assert got == want

def test_twoSum3():
	got = twoSum([3,3],6)
	want = (0,1)

	assert got == want

# first attempt, nested loops @ O(n^2)
# def twoSum(nums: List[int], target: int):
# 	# loop through the array
# 	for index1, item1 in enumerate(nums):
# 		# loop through the items starting after this one
# 		for index2 in range(index1+1, len(nums)):
# 			# if the outer loop value + inner loop value == target
# 			if item1 + nums[index2] == target:
# 				# return their indices as a list
# 				return [index1, index2]
# 	# default to return False
# 	return False

"""
LeetCode:
	Runtime: 3244ms
	Memory Usage: 14.9MB
"""

# second attempt using a dictionary
def twoSum(nums: List[int], target: int):
	# create a dictionary to hold items we've checked
	dict = {}

	# loop through the array
	for index, num in enumerate(nums):
		# if the difference between the target and this item is in dict
		# we've found the second value
		if target - num in dict:
			# return the dict value's index and this index
			return dict[target - num], index
		# otherwise, put this item in dict
		dict[num] = index

	# default to return False
	return False

"""
LeetCode:
	Runtime: 114ms
	Memory Usage: 15.3MB
"""

if __name__ == "__main__":
	print(twoSum([2,7,11,15], 9))
	print(twoSum([3,2,4],6))
	print(twoSum([3,3],6))