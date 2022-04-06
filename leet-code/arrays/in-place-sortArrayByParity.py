from typing import List

"""
	Given an array of integers,
	move all the even integers to the beginning of the array
	followed by all the odd integers.
	Return any array that satisfies this condition
"""

def test_sortArrayByParity1():
	got = sortArrayByParity([3,1,2,4])
	want = [2,4,3,1]

	assert got == want

def test_sortArrayByParity2():
	got = sortArrayByParity([0])
	want = [0]

	assert got == want

# slightly more memory-intensive, but faster
def sortArrayByParity(nums: List[int]):
    # create a list to store even numbers
	evens = []

	# create a list to store odd numbers
	odds = []

	# loop over array
	for index, item in enumerate(nums):
		# if this number is even
		if item % 2 == 0:
			# add it to the even array
			evens.append(item)
		# otherwise, it's odd
		else:
			# add it to the odd array
			odds.append(item)

	# combine the even array, odd array, and zero arrays
	mergedList = evens + odds

	# return the combined array
	return mergedList

if __name__ == "__main__":
	print(sortArrayByParity([3,1,2,4]))
	print(sortArrayByParity([0]))

"""
LeetCode:
	Runtime: 117ms
	Memory Usage: 14.7MB
"""

# slower, but slightly less memory intensive
def sortArrayByParity2(nums: List[int]):
    # set an index for odd numbers
    odd = 0

    # loop through the array
    for index in range(len(nums)):
        # if this item is an even number
        if nums[index] % 2 == 0:
            # swap it with the number at the odd index
            nums[index], nums[odd] = nums[odd], nums[index]
            # increment the odd index
            odd += 1

    # return the array
    return nums

if __name__ == "__main__":
	print(sortArrayByParity2([3,1,2,4]))
	print(sortArrayByParity2([0]))

"""
LeetCode:
	Runtime: 161ms
	Memory Usage: 14.6MB
"""