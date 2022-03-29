import pytest
from typing import List

"""
	Given two integer arrays (`nums1` and `nums2`) sorted in ascending order,
	and two integers, `m` = length of turned on digits in `nums1`,
					  `n` = length of digits in `nums2`.
	Merge `nums1` and `nums2` together in ascending order.
	Store the merged array in `nums1`
"""
def test_merge():
	got = merge([1,2,3,0,0,0],3,[2,5,6],3)
	want = [1,2,2,3,5,6]

	assert got == want

def test_merge2():
	got = merge([1],1,[],0)
	want = [1]

	assert got == want

def test_merge3():
	got = merge([0],0,[1],1)
	want = [1]

	assert got == want

def merge(nums1: List[int], m: int, nums2: List[int], n: int):
	"""
	Find the largest value between nums1 and nums2.
	Move the largest value to the last open spot in nums1.
	Do not return anything, modify nums1 in-place instead.
	"""
	# last index of nums1 array
	end = len(nums1)-1

	# loop while there are values in nums2 that haven't been moved
	while n > 0:
		# if there's nothing left in nums1 to move
		# or the value in nums2 is larger
		if m <= 0 or nums2[n-1] > nums1[m-1]:
			# move the largest nums2 value to the last open spot in nums1
			nums1[end] = nums2[n-1]
			# decrement the counter for nums2
			n -= 1
		else:
			# move the largest nums1 value to the last open spot in nums1
			nums1[end] = nums1[m-1]
			# decrement the counter for nums1
			m -= 1
		# decrement the last index for nums1
		end -= 1

	return nums1

if __name__ == "__main__":
	print(merge([1,2,3,0,0,0],3,[2,5,6],3))
	print(merge([1],1,[],0))
	print(merge([0],0,[1],1))