from typing import List

"""
	Given an array of integers,
	return True if it's a valid mountain array
"""

def test_validMountainArray1():
	got = validMountainArray([2,1])
	want = False

	assert got == want

def test_validMountainArray2():
	got = validMountainArray([3,5,5])
	want = False

	assert got == want

def test_validMountainArray3():
	got = validMountainArray([0,3,2,1])
	want = True

	assert got == want

def validMountainArray(arr: List[int]):
	# only check if the array has 3 or more values
	if len(arr) >= 3:
		# pointer that starts at beginning (left-side) and moves to the right
		leftPointer = 0
		# pointer that starts at the end (right-side) and moves to the left
		rightPointer = len(arr)-1

		# while the next index is not the last index of the array
		# and while this value is less than the next value
		while leftPointer + 1 < len(arr)-1 and arr[leftPointer] < arr[leftPointer + 1]:
			# move to the next index
			leftPointer += 1

		# while the previous index is not the first index
		# and while this value is less than the previous value
		while rightPointer - 1 > 0 and arr[rightPointer] < arr[rightPointer - 1]:
			# move to the previous index
			rightPointer -= 1

		# if our pointers stopped on the same value
		# this is a valid mountain array
		if leftPointer == rightPointer:
			return True

	# default to return False
	return False

if __name__ == "__main__":
	print(validMountainArray([2,1]))
	print(validMountainArray([3,5,5]))
	print(validMountainArray([0,3,2,1]))
	print(validMountainArray([0,1,2,3,4,5,6,7,8,9]))

"""
LeetCode:
	Runtime: 230ms
	Memory Usage: 15.3MB
"""