class Solution():

    def __init__(self):
        self.stack = []


    def isValid(self, s):

        brackets = {"(": ")", "{": "}", "[": "]"}

        for parenthese in s:
            if parenthese in brackets:
                self.stack.append(parenthese)
            elif len(self.stack) == 0 or brackets[self.stack.pop()] != parenthese:
                return False

        return not len(self.stack)


S = Solution()
print (S.isValid("[()]") )
