from typing import List

"""
	Given an array of integers,
	replace every element in the array
	with the greatest element among the elements to the right
	and replace the last element with -1.
	Return the array.
"""

def test_replaceElements1():
	got = replaceElements([17,18,5,4,6,1])
	want = [18,6,6,6,1,-1]

	assert got == want

def test_replaceElements2():
	got = replaceElements([400])
	want = [-1]

	assert got == want

def replaceElements(arr: List[int]):
	# set the highestValue to -1
	highestValue = -1

	# walk through each element in the array from front to back
	for index in range(len(arr)-1, -1, -1):
		# set this element to highestValue
		# and set the highestValue to whichever is larger - the highestValue or this element
		arr[index], highestValue = highestValue, max(highestValue, arr[index])

	return arr

if __name__ == "__main__":
	print(replaceElements([17,18,5,4,6,1]))
	print(replaceElements([400]))

"""
LeetCode:
	Runtime: 167ms
	Memory Usage: 15.2MB
"""