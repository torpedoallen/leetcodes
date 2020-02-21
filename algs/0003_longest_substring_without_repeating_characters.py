






'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''



from collections import OrderedDict

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        d = OrderedDict()
        max_ = 0
        len_ = 0
        for ch in s:
            while ch in d:
                len_ -= 1
                d.popitem(last=False)
            d[ch] = 1
            len_ += 1
            max_ = max(len_, max_)
        return max_



if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring('abcabcbb'))
    print(Solution().lengthOfLongestSubstring('bbbbb'))
    print(Solution().lengthOfLongestSubstring('qrsvbspk'))
    print(Solution().lengthOfLongestSubstring('aab'))
    print(Solution().lengthOfLongestSubstring(None))
