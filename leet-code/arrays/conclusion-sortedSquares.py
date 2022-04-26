from typing import List

"""
	Given an array of integers `nums`,
	sorted in ascending order,
	return an array of the squares of each number in ascending order.
"""

def test_sortedSquares1():
	got = sortedSquares([-4,-1,0,3,10])
	want = [0,1,9,16,100]

	assert got == want

def test_sortedSquares2():
	got = sortedSquares([-7,-3,-2,3,11])
	want = [4,9,9,49,121]

	assert got == want

def sortedSquares(nums: List[int]):
	# square every digit
	for index in range(len(nums)):
		nums[index] = nums[index] * nums[index]

	# order by ascending
	nums.sort()

	# return the original array
	return nums

if __name__ == "__main__":
	print(sortedSquares([-4,-1,0,3,10]))
	print(sortedSquares([-7,-3,-2,3,11]))

"""
LeetCode:
	Runtime: 274ms
	Memory Usage: 15.8MB
"""

# pythonic way
def sortedSquares(nums: List[int]):
	# square every digit and return a sorted list
	return sorted(digit*digit for index, digit in enumerate(nums))

if __name__ == "__main__":
	print(sortedSquares([-4,-1,0,3,10]))
	print(sortedSquares([-7,-3,-2,3,11]))

"""
LeetCode:
	Runtime: 218ms
	Memory Usage: 16.4MB
"""