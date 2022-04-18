from typing import List

"""
	Given an array of integers `heights`,
	create an array `expected` where the integers are in ascending order,
	return the number of indices where `heights[i] != expected[i]`.
"""

def test_heightChecker1():
	got = heightChecker([1,1,4,2,1,3])
	want = 3

	assert got == want

def test_heightChecker2():
	got = heightChecker([5,1,2,3,4])
	want = 5

	assert got == want

def test_heightChecker3():
	got = heightChecker([1,2,3,4,5])
	want = 0

	assert got == want

def heightChecker(heights: List[int]):
	# copy heights to expected
	expected = heights[:]
	# sort expected in ascending order
	expected.sort()
	# create a variable to hold the different indices
	different = 0

	# compare the 2 lists to see which indices hold a different value
	for i in range(len(heights)):
		if heights[i] != expected[i]:
			different += 1

	# return the number of indices that are not equal
	return different

if __name__ == "__main__":
	print(heightChecker([1,1,4,2,1,3]))
	print(heightChecker([5,1,2,3,4]))
	print(heightChecker([1,2,3,4,5]))

"""
LeetCode:
	Runtime: 46ms
	Memory Usage: 13.9MB
"""

# # one-line option
# def heightChecker(heights: List[int]):
# 	# iterate over heights and a sorted heights list
# 	# return the sum of indices where they don't match
# 	return sum(x != y for x, y in zip(heights, sorted(heights)))

# if __name__ == "__main__":
# 	print(heightChecker([1,1,4,2,1,3]))
# 	print(heightChecker([5,1,2,3,4]))
# 	print(heightChecker([1,2,3,4,5]))

"""
LeetCode:
	Runtime: 40ms
	Memory Usage: 13.8MB
"""