import pytest
from typing import List

"""
	Given a fixed-length integer array `arr`,
	duplicate each occurrence of zero, 
	shifting the remaining elements to the right.
"""
def test_duplicateZeros():
	got = duplicateZeros([1,0,2,3,0,4,5,0])
	want = [1,0,0,2,3,0,0,4]

	assert got == want

def duplicateZeros(arr: List[int]):
	# create an array to hold the new values
	zerosArray = []
	# track the length of the original arr
	originalLenth = len(arr)

	# step through each digit in the original array
	for digit in arr:
		# add it to the new array
		zerosArray.append(digit)
		# if there's a 0 digit
		if digit == 0:
			# add an extra 0 to the new array
			zerosArray.append(0)

	# loop through as many times as the length of the original array
	for index in range(originalLenth):
		# replace the element in the original array with the zerosArray element
		arr[index] = zerosArray[index]

	return arr

if __name__ == "__main__":
	print(duplicateZeros([1,0,2,3,0,4,5,0]))