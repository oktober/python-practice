from typing import List

"""
	Given an array `nums` of `n` integers,
	where `nums[i]` is in the range [1,n],
	return an array of all the integers in the range [1,n]
	that do not appear in `nums`.
"""

def test_findDisappearedNumbers1():
	got = findDisappearedNumbers([4,3,2,7,8,2,3,1])
	want = [5,6]

	assert got == want

def test_findDisappearedNumbers2():
	got = findDisappearedNumbers([1,1])
	want = [2]

	assert got == want

def findDisappearedNumbers(nums: List[int]):
	# my original solution
	# create a unique set of numbers
	unique = set(nums)
	# create a new list to store the results
	disappeared = []

	# loop from 1 to length of nums+1 (to loop n times total)
	for digit in range(1,len(nums)+1):
		# if this number is not in our unique set
		if digit not in unique:
			# add it to disappeared
			disappeared.append(digit)

	return disappeared
	"""
	LeetCode:
		Runtime: 411ms
		Memory Usage: 24.7MB
	"""

	# # pythonic way
	# unique = set(nums)
	# return [digit for digit in range(1, len(nums)+1) if digit not in unique]
	"""
	LeetCode:
		Runtime: 413ms
		Memory Usage: 24.4MB
	"""

	# # pythonic way using only original array
	# for index in range(len(nums)):
	# 	# get the absolute value for this index
	# 	absDigit = abs(nums[index])
	# 	# if the value at the index before this absolute value is positive
	# 		# since we're starting at 1, not 0 for the values we're looking for
	# 		# e.g. the 4th spot would be found at nums[4-1] -> nums[3]
	# 	if nums[absDigit-1] > 0:
	# 		# set it to a negative number - mark it as "found"
	# 		nums[absDigit-1] = nums[absDigit-1] * -1

	# # return the index+1 (to get values from 1 to n) if this value was not "found"
	# 	# i.e. if it was not marked negative
	# return [index+1 for index in range(len(nums)) if nums[index] > 0]
	"""
	LeetCode:
		Runtime: 705ms
		Memory Usage: 22.2MB
	"""

if __name__ == "__main__":
	print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
	print(findDisappearedNumbers([1,1]))
