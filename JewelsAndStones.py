class Solution(object):
    def numJewelsInStones(self, J, S):
        result = 0
        for i in range(0, len(J)):
            result += S.count(J[i])
        return result


s = Solution()
print(s.numJewelsInStones("z", "ZZ"))