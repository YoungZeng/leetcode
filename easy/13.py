'''
首先建立一个HashMap来映射符号和值，然后对字符串从左到右来，
如果当前字符代表的值小于其右边，就减去该值；否则就加上该值
'''


class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        for i in range(len(s) - 1):
            if d.get(s[i]) < d.get(s[i + 1]):
                result -= d.get(s[i])
            else:
                result += d.get(s[i])
        return result + int(d.get(s[-1]))