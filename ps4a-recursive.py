def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    # '''

    permutations = []

    if len(sequence) == 1:
        permutations += sequence[0]
    else:
        for index,letter in enumerate(sequence):
            # get the other letters and put them in a string
            other_letters = ''
            for index2, chars in enumerate(sequence):
                if index2 != index:
                    other_letters += chars

            # for each other letter in the string, recursively call this function until we hit the base case
            sublist = get_permutations(other_letters)

            # once we get back a permutation, append it to build the permutation string
            for l in sublist:
                permutations.append(letter + l)

    # Use a set to only return unique values, no duplicates
    permutations = (list(set(permutations)))

    return permutations

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    test1 = 'a'
    print('Input:', test1)
    print('Expected Output:', ['a'])
    print("----")
    print('Actual Output:', get_permutations(test1))
    print("---------------------------")

    test2 = 'ab'
    print('Input:', test2)
    print('Expected Output:', ['ab', 'ba'])
    print("----")
    print('Actual Output:', get_permutations(test2))
    print("---------------------------")

    test3 = 'abc'
    print('Input:', test3)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print("----")
    print('Actual Output:', get_permutations(test3))
    print("---------------------------")

    test3 = 'abb'
    print('Input:', test3)
    print('Expected Output:', ['abb', 'bab', 'bba'])
    print("----")
    print('Actual Output:', get_permutations(test3))
    print("---------------------------")
