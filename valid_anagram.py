class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        qList = {}
        for i in s:
            if i not in qList:
                qList[i] = 1
            else:
                x = qList[i]+1
                qList[i] = x
        for j in t:
            if j in qList:
                x = qList[j]-1
                qList[j] = x
            else:
                return False
        for key, value in qList.items():
            if value != 0:
                return False
        return True