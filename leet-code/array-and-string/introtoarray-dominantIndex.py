from typing import List

"""
	Given an array of integers `nums`,
	where the largest integer is unique,
	determine whether the largest element
	is at least twice as much as every other number.
	If it is, return the index of the largest element,
	otherwise return -1.
"""

def test_dominantIndex1():
	got = dominantIndex([3,6,1,0])
	want = 1

	assert got == want

def test_dominantIndex2():
	got = dominantIndex([1,2,3,4])
	want = -1

	assert got == want

def test_dominantIndex3():
	got = dominantIndex([1])
	want = 0

	assert got == want

# original code using a dictionary
# def dominantIndex(nums: List[int]):
	# # if there are any values in the list
	# if nums:
	# 	# create a variable to hold the current largest
	# 	digitDict = {'largest': 0, 'largestIndex': 0, 'secondLargest': 0, 'secondLargestIndex': 0}

	# 	# go through the list
	# 	for index, value in enumerate(nums):
	# 	# if this value is > digitDict['largest']
	# 		if value > digitDict['largest']:
	# 		# move largest to secondLargest
	# 			digitDict['secondLargest'], digitDict['secondLargestIndex'] = digitDict['largest'], digitDict['largestIndex']
	# 		# replace largest with this value
	# 			digitDict['largest'], digitDict['largestIndex'] = value, index
	# 	# elif this value is > digitDict['secondLargest']
	# 		elif value > digitDict['secondLargest']:
	# 		# replace secondLargest with this value
	# 			digitDict['secondLargest'], digitDict['secondLargestIndex'] = value, index

	# 	# if the largest value is greater than or equal to the second largest value * 2
	# 	if digitDict['largest'] >= digitDict['secondLargest'] * 2:
	# 		# return the index of largest
	# 		return digitDict['largestIndex']
	# 	# otherwise, return -1
	# 	else:
	# 		return -1

	# # default to return -1
	# return -1

# if __name__ == "__main__":
# 	print(dominantIndex([3,6,1,0]))
# 	print(dominantIndex([1,2,3,4]))
# 	print(dominantIndex([1]))

"""
LeetCode:
	Runtime: 41ms
	Memory Usage: 13.8MB
"""

# optimized to use less code, faster but uses slightly more memory
def dominantIndex(nums: List[int]):
	if nums:
		# get the largest number from the array
		largest = max(nums)
		# get the index for that number
		largestIndex = nums.index(largest)

		if len(nums) > 1:
			# remove the largest element
			nums.pop(largestIndex)

			# get the next largest number
			secondLargest = max(nums)

			# if the largest is double the second largest, or greater
				# return the index of the largest number
			return largestIndex if largest >= secondLargest * 2 else -1
		else:
			# if there's only one value in the array
			# the only number will always be twice the value of any other number
			return largestIndex

	# default to return -1
	return -1


if __name__ == "__main__":
	print(dominantIndex([3,6,1,0]))
	print(dominantIndex([1,2,3,4]))
	print(dominantIndex([1]))

"""
LeetCode:
	Runtime: 27ms
	Memory Usage: 13.9MB
"""