import pytest
from typing import List

"""
	Given a fixed-length integer array `nums`,
	delete every instance of `val`, 
	shifting the remaining elements to the left.
"""
def test_removeElement1():
	got = removeElement([3,2,2,3], 3)
	want = [2,2]

	assert got == want

def test_removeElement2():
	got = removeElement([0,1,2,2,3,0,4,2], 2)
	want = [0,1,3,0,4]

	assert got == want

# my original answer
# def removeElement(nums: List[int], val: int):
# 	# flag to stop while loop
# 	# set to true initially so loop runs at least once
# 	found = True

# 	while(found):
# 	    # set to false so if no vals are found the loop will stop
# 		found = False
		
# 	    # loop through the array
# 		for index,item in enumerate(nums):
# 			# if this is a val
# 			if item == val:
# 				# take everything after this index and put it in the array at this index
# 				nums[index:] = nums[index+1:]
	            
# 	            # add this to append an 'x' if you want to keep the array length the same
# 				# nums.append('x')
				
# 				# set found flag to run the loop again
# 				found = True

# 	return nums

# way simpler answer using python helpers
def removeElement(nums: List[int], val: int):
	while val in nums:
		nums.remove(val)

	return nums

if __name__ == "__main__":
	print(removeElement([3,2,2,3], 3))
	print(removeElement([0,1,2,2,3,0,4,2], 2))