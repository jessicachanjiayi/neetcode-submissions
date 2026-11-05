class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        countS = {}
        countT = {}
        
        for i in range(len(s)):
            countS[s[i]]= 1+ countS.get(s[i],0)
            countT[t[i]]= 1+ countT.get(t[i],0)
            # 统计词频，自己本身是一个1，如果s[i]存在于词典里，就去get s[i]这个key对应的value, otherwise get 0 如果词典里没有这个key存在
        return countS == countT