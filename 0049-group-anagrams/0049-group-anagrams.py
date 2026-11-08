class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res={}
        
        for s in strs:
            a=[0]*26
            for i in s:
                a[ord(i)-ord('a')]+=1
            a=tuple(a)
            if a not in res:
                
                res[a]=[s]
            else:
                res[a].append(s)

        return(list(res.values()))
         
          
        