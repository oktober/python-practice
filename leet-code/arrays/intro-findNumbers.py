import pytest
from typing import List

""" Given an array of `nums`, return how many of them contain an even number of digits """
def test_findNumbers():
	got = findNumbers([12,345,2,6,7896])
	want = 2

	assert got == want

def findNumbers(nums: List[int]):
	evens = 0

	for number in nums:
		if len(str(number)) % 2 == 0:
			evens += 1

	return evens

if __name__ == "__main__":
	print(findNumbers([12,345,2,6,7896]))
