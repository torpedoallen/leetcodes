










'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zigzag-conversion
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



class Solution(object):



    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = len(s)
        if n == 0:
            return ''
        if numRows <= 1:
            return s
        width = (n // (2*numRows - 2) + 1)*(numRows-1)
        marked = [[None for _ in range(width)] for i in range(numRows)]
        patterns = [(1, 0) for i in range(numRows - 1)] + [(-1, 1) for i in range(numRows - 1)]
        i, j = 0, 0
        idx = 0
        marked[0][0] = s[0]
        while idx < (n-1):
            for di in patterns:
                i = i + di[0]
                j = j + di[1]
                idx += 1
                marked[i][j] = s[idx]
                if idx == n - 1:
                    break

        ret = []
        for i in range(numRows):
            for j in range(width):
                if marked[i][j] is not None:
                    ret.append(marked[i][j])
        return ''.join(ret)


print(Solution().convert('PAYPALISHIRING', 4))
print(Solution().convert('', 4))
print(Solution().convert('PAY', 4))
print(Solution().convert('AB', 1))
print(Solution().convert('AB', 0))
