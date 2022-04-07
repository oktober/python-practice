from typing import List

"""
	Given an array of integers `nums` and an integer `val`,
	remove all occurrences of `val` in `nums` in-place.
	Do not allocate space for another array.
"""

def test_removeElement1():
	got = removeElement([3,2,2,3],3)
	want = 2

	assert got == want

def test_removeElement2():
	got = removeElement([0,1,2,2,3,0,4,2],2)
	want = 5

	assert got == want

# code with one fast pointer (index) and one slow pointer (valIndex)
# this will run faster if there are more `val`s in `nums`
def removeElement(nums: List[int], val: int):
	# create a variable to track the index of val
	valIndex = 0

	# loop through each item in the array
	for index in range(len(nums)):
		# if this element is not equal to val
		if nums[index] != val:
			# replace the element at valIndex with this element
			nums[valIndex] = nums[index]
			# increment valIndex
			valIndex += 1
		print(nums)
		print("----------")

	# return the length of the remaining elements
	return valIndex

if __name__ == "__main__":
	print(removeElement([3,2,2,3],3))
	print(removeElement([0,1,2,2,3,0,4,2],2))

"""
LeetCode:
	Runtime: 28ms
	Memory Usage: 13.8MB
"""

# code with one pointer at end and one at beginning
# this will run faster if there are less `val`s in `nums`
def removeElement2(nums: List[int], val: int):
	# set the first pointer to start at the beginning
	index = 0
	# set the second pointer to start at the end
	n = len(nums)

	# loop while the first pointer hasn't reached the second pointer
	while (index < n):
		# if this element is equal to val
		if nums[index] == val:
			# swap it with the element at the second pointer
			nums[index] = nums[n-1]
			# decrement the second pointer
			n -= 1
		else:
			# increment the first pointer
			index += 1
	# return the second pointer to count how many non-vals we have
	return n

if __name__ == "__main__":
	print(removeElement2([3,2,2,3],3))
	print(removeElement2([0,1,2,2,3,0,4,2],2))

"""
LeetCode:
	Runtime: 43ms
	Memory Usage: 13.9MB
"""