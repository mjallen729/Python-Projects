"""Find the longest palindromic substring.

Locate the longest palindromic substring in a given string and
return it.
"""

def find_palindrome(s:str) -> str:
    # hello
    # at each point, traverse grab all chars behind (inclusive)
    # reverse it and see if it matches current 
    # if it does, compare it to longest. set longest to max length

    start_index = 0
    diff = str()
    longest = str()

    for i in range(len(s)):
        diff = s[start_index:i+1]
        diff = diff[::-1]
        #print(diff)

        if diff == s[start_index:i+1]:  # if palindrome
            if len(diff) > len(longest):
                longest = diff

        else:  # if not a palindrome, update start index
            #start_index = i
            pass
            

    return longest


print(find_palindrome("hello"))