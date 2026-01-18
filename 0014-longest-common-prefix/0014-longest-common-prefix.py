class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 그냥 앞글자 따서 하면 될듯
        if "" in strs:
            return ""
        if len(strs) < 2:
            return strs[0]
        result = ""
        temp = ""
        for i in strs[0]:
            temp += i
            for j in range(0, len(strs)):
                print(strs[j], temp)
                if not strs[j].startswith(temp):
                    return result
            result = temp
        return result
                
                

        