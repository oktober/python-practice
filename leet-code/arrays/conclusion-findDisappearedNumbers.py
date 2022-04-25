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

# this code exceeds the time limit
def findDisappearedNumbers(nums: List[int]):
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

if __name__ == "__main__":
	print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))
	print(findDisappearedNumbers([1,1]))

"""
LeetCode:
	Runtime: 411ms
	Memory Usage: 24.7MB
"""