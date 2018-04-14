class Solution(object):
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        s = ''.join(sorted(s))
        t = ''.join(sorted(t))

        for i in range(len(s)):
            if s[i] != t[i]:
                return False

        return True


s = Solution()
print(s.isAnagram("anagram","nagaram"))