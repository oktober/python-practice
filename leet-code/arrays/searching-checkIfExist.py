from typing import List

"""
	Given an array,
	check if N and its double (M) exist
"""

def test_checkIfExist1():
	got = checkIfExist([10,2,5,3])
	want = True

	assert got == want

def test_checkIfExist2():
	got = checkIfExist([7,1,14,11])
	want = True

	assert got == want

def test_checkIfExist3():
	got = checkIfExist([3,1,7,11])
	want = False

	assert got == want

'''
	Check if there exists 2 indices i and j such that:
	i != j
	0 <= i, j < arr.length
	arr[i] == 2 * arr[j]
'''

def checkIfExist(arr: List[int]):
	# loop through the array
	for i in range(len(arr)):
		# if this value doubled is in array
		# and it has a different index
		if arr[i] * 2 in arr and arr.index(arr[i] * 2) != i:
			# stop the loop and return True
			return True
	# otherwise, we'll return false because we didn't find the double
	return False

if __name__ == "__main__":
	print(checkIfExist([10,2,5,3]))
	print(checkIfExist([7,1,14,11]))
	print(checkIfExist([3,1,7,11]))
	print(checkIfExist([-2,0,10,-19,4,6,-8]))