class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest_index = 0
        max_length = 0
        for i in xrange(len(s)):
            if is_palindrome(s, i - max_length, i):
                longest_index = i - max_length
                max_length = max_length + 1
            elif i - max_length - 1 >= 0 and is_palindrome(s, i - max_length - 1, i):
                longest_index = i - max_length - 1
                max_length = max_length + 2

        return s[longest_index:longest_index + max_length]

def is_palindrome(string, start, end):
    return string[start:end+1] == string[start:end+1][::-1]