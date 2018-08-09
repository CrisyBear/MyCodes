# We are given two strings, A and B.
# A shift on A consists of taking string A and moving the leftmost character to the rightmost position.
# For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if
# A can become B after some number of shifts on A.
# Example 1:
# Input: A = 'abcde', B = 'cdeab'
# Output: true
# Example 2:
# Input: A = 'abcde', B = 'abced'
# Output: false
class Solution:
    def rotateString(self, A, B):
        a = list(A)
        b = list(B)
        if (len(A) != len(B)):
            return False
        if (len(A) == 0):
            return True
        if (len(A)) > 100:
            return False
        for i in range(len(A)):
            alast = a[0]
            del a[0]
            a.append(alast)
            if (a == b):
                return True
        return False


A = 'abcde'
B = 'deabc'
test = Solution()
s = test.rotateString(A, B)
if s == True:
    print("true")
else:
    print('false')

A = 'abcde'
B = 'abced'
test = Solution()
s = test.rotateString(A, B)
if s == True:
    print("true")
else:
    print('false')

A = ''
B = ''
test = Solution()
s = test.rotateString(A, B)
if s == True:
    print("true")
else:
    print('false')

A = ''
B = 'a'
test = Solution()
s = test.rotateString(A, B)
if s == True:
    print("true")
else:
    print('false')