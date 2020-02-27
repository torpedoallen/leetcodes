'''
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
'''




class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        signed = 1 if divisor*dividend > 0 else -1
        divisor = abs(divisor)
        dividend = abs(dividend)
        seed = 0
        quot = 0
        for i in range(31, -1, -1):
            if seed + (divisor << i) <= dividend:
                seed += divisor << i # 累计 & 累加倍数
                quot += 1 << i
        return min(quot*signed, (2<<30)-1)
