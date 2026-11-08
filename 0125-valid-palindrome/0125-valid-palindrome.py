class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        print(s)
        l=0
        r=len(s)-1
        while l<r:
            if not s[l].isalnum() :
                l=l+1
            elif not s[r].isalnum():
                r=r-1
            elif s[l]!=s[r]:
                return False
            else:
                r=r-1
                l=l+1
            
        return True


        