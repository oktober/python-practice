from typing import List

"""
	Given a string `s`
	containing just the characters:
	'(', ')', '{', '}', '[', ']'
	determine if the input string is valid:
		- Open brackets must be closed by same type of brackets
		- Open brackets must be closed in the correct order
"""

def test_isValid1():
	got = isValid("()")
	want = True

	assert got == want

def test_isValid2():
	got = isValid("()[]{}")
	want = True

	assert got == want

def test_isValid3():
	got = isValid("(]")
	want = False

	assert got == want

def isValid(s: str):
    # dictionary of right: left bracket pairs
    bracketPairs = {")" : "(", "}" : "{", "]" : "["}

    # LIFO array/list to keep track of uncompleted bracket pairs
    lifo = []

    # loop through string
    for char in s:
        
        # if we hit a right bracket and 
        # `lifo` is empty or
        # the last element in `lifo` is NOT its corresponding left bracket
        if char in bracketPairs.keys() and (not lifo or lifo[-1] != bracketPairs[char]):
            # return False and exit since this bracket pair is incorrect
            return False
        
        # elif we hit a left bracket
        elif char in bracketPairs.values():
            # add it to the end of `lifo`
            lifo.append(char)
        
        # elif we hit a right bracket and there's values in `lifo` and
        # the last element in `lifo` IS its corresponding left
        elif char in bracketPairs.keys() and lifo and lifo[-1] == bracketPairs[char]:
            # remove the left bracket from the end of `lifo`
            lifo.pop(-1)

    # if we've gone through all the char's of `s` and
    # `lifo` is empty
    if not lifo:
        # this means there are no un-paired brackets left
        return True

    # default to return False
    return False

if __name__ == "__main__":
	print(isValid("()"))
	print(isValid("()[]{}"))
	print(isValid("(]"))

"""
LeetCode:
	Runtime: 24ms
	Memory Usage: 13.9MB
"""