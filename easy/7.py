class Solution:
    def reverse(self, x: int) -> int:
        if x < -(2 ** 31) or x > (2 ** 31) -1:
            return 0
        factor = 1
        if x < 0:
            factor = -1
        result = factor * int(str(factor * x)[::-1])
        if result < -(2 ** 31) or result > (2 ** 31) -1:
            return 0
        return result