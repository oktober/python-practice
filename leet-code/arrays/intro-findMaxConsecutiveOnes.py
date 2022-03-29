import pytest
from typing import List

""" Give a binary array `nums`, return the maximum number of consecutive 1's in the array """
def test_findMaxConsecutiveOnes():
	got = findMaxConsecutiveOnes([1,1,0,1,1,1])
	want = 3

	assert got == want

def findMaxConsecutiveOnes(nums: List[int]):
	consecutive = 0
	highest = 0
	for digit in nums:
		if digit == 1:
			consecutive += 1
			highest = max(highest, consecutive)
		else:
			consecutive = 0

	return highest

if __name__ == "__main__":
	print(findMaxConsecutiveOnes([1,1,0,1,1,1]))
