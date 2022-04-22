from typing import List

"""
	Given an array of integers `nums`,
	return the third distinct maximum number.
	If doesn't exist, return the maximum number.
"""

def test_thirdMax1():
	got = thirdMax([3,2,1])
	want = 1

	assert got == want

def test_thirdMax2():
	got = thirdMax([1,2])
	want = 2

	assert got == want

def test_thirdMax3():
	got = thirdMax([2,2,3,1])
	want = 1

	assert got == want

# def thirdMax(nums: List[int]):
# 	# use set to get rid of extraneous numbers
# 	nums = list(set(nums))

# 	# order array by increasing
# 	nums.sort(reverse=True)

# 	# return the 3rd element or, if doesn't exist, return the first element
# 	if len(nums) >= 3:
# 		return nums[2]
# 	else:
# 		return nums[0]

# if __name__ == "__main__":
# 	print(thirdMax([3,2,1]))
# 	print(thirdMax([1,2]))
# 	print(thirdMax([2,2,3,1]))

"""
LeetCode:
	Runtime: 91ms
	Memory Usage: 15.6MB
"""

def thirdMax(nums: List[int]):
	# create a list of 3 negative infinity numbers
    comparisonList = [float('-inf'), float('-inf'), float('-inf')]

    # loop through each digit in nums
    for num in nums:
    	# if we haven't put this digit in our comparisonList
        if num not in comparisonList:
        	# check if this number is larger than the first value in comparisonList
            if num > comparisonList[0]:   
            	# put it as the first value and move the others to the right
            	comparisonList = [num, comparisonList[0], comparisonList[1]]
        	# check if this number is larger than the second value
            elif num > comparisonList[1]: 
            	# put it as the first value and move the original value to the right
            	comparisonList = [comparisonList[0], num, comparisonList[1]]
        	# check if this number is larger than the third value
            elif num > comparisonList[2]: 
            	# put it as the third value
            	comparisonList[2] = num

	# return the maximum value of nums if we don't have 3 nums digits in comparisonList
		# otherwise, return the 3rd digit of comparisonList
    return max(nums) if float('-inf') in comparisonList else comparisonList[2]

if __name__ == "__main__":
	print(thirdMax([3,2,1]))
	print(thirdMax([1,2]))
	print(thirdMax([2,2,3,1]))

"""
LeetCode:
	Runtime: 62ms
	Memory Usage: 14.8MB
"""