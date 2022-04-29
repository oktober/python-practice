from typing import List

"""
	Given a large integer represented as an array of `digits`,
	increment the large integer by one and
	return the resulting array of digits.
"""

def test_plusOne1():
	got = plusOne([1,2,3])
	want = [1,2,4]

	assert got == want

def test_plusOne2():
	got = plusOne([4,3,2,1])
	want = [4,3,2,2]

	assert got == want

def test_plusOne3():
	got = plusOne([9,9])
	want = [1,0,0]

	assert got == want

def plusOne(digits: List[int]):
	# loop over array backwards, starting from the last item
	for index in reversed(range(len(digits))):
		# if this element is a 9
		if digits[index] == 9:
			# set the element to be 0
			digits[index] = 0
		else:
			# increment the digit by one
			digits[index] += 1
			# break out of the loop
			break
	# if the first element is a 0
	if digits[0] == 0:
		# insert a 1 as the new first element
		digits.insert(0, 1)

	# return the array
	return digits

if __name__ == "__main__":
	print(plusOne([1,2,3]))
	print(plusOne([4,3,2,1]))
	print(plusOne([9,9]))

"""
LeetCode:
	Runtime: 42ms
	Memory Usage: 13.7MB
"""