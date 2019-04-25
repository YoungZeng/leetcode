'''
利用python的max()和min()，
在Python里字符串是可以比较的，按照ascII值排，举例abb， aba，abac，最大为abb，最小为aba。
所以只需要比较最大最小的公共前缀就是整个数组的公共前缀。
法一法二不相上下。
'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs_max = max(strs)
        strs_min = min(strs)
        if strs_max == strs_min:  # 企图加速
            return strs_max

        # 两种处理方式
        for i in range(len(strs_min)):  # 一
            if strs_min[i] != strs_max[i]:
                return strs_min[:i]

        # for i, value in enumerate(strs_min):  # 二
        #     if value != strs_max[i]:
        #         return strs_max[:i]

        return strs_min
