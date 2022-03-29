import pytest
from typing import List

""" 
	Given an integer array `nums` sorted in non-decreasing order, 
	return an array of the squares of each number sorted in non-decreasing order
"""
def test_sortedSquares():
	got = sortedSquares([-4,-1,0,3,10])
	want = [0,1,9,16,100]

	assert got == want

def sortedSquares(nums: List[int]):
	squares = []
	for number in nums:
		squares.append(number * number)

	squares.sort()

	return squares
	
if __name__ == "__main__":
	print(sortedSquares([-4,-1,0,3,10]))
