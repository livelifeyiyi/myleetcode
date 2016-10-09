class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.strip().split(' ')
        len_s = len(words)
        #if len_s == 1:
        #    return 0
        #else:
        return len(words[len_s-1])

S = Solution()
print S.lengthOfLastWord("a a")