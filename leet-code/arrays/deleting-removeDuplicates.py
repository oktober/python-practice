import pytest
from typing import List

"""
	Given a fixed-length integer array `nums`,
	keep only the first instance of every number, 
	shifting the remaining elements to the left.
"""
def test_removeDuplicates1():
	got = removeDuplicates([1,1,2])
	want = 2

	assert got == want

def test_removeDuplicates2():
	got = removeDuplicates([0,0,1,1,2,2,3,3,4])
	want = 5

	assert got == want

def removeDuplicates(nums: List[int]):
    # if the array is empty
	if not nums:
        # set the length to 0
		length = 0
    # if the array is not empty
	else:
        # set the length of the non-duplicated array to 1
		length = 1
        # start the index at 0
		index = 0

		# loop through all the values starting with the second one
		for index2 in range(1, len(nums)):
			
			# if this is not a duplicate value
			if nums[index2] != nums[index]:
				# move the index to the next spot
				index += 1
                # move the non-duplicate value to this spot
				nums[index] = nums[index2]
				# increase the length of the non-duplicated array
				length += 1

    # return the length of the non-duplicated array
	return length

if __name__ == "__main__":
	print(removeDuplicates([1,1,2]))
	print(removeDuplicates([0,0,1,1,2,2,3,3,4]))