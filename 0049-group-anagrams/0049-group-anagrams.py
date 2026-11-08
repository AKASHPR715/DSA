class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = {} 
        for s in strs:
            a = [0] * 26  # Initialize frequency array for 26 lowercase letters
            for i in s:
                a[ord(i) - ord('a')] += 1  # Count frequency of each character
            a = tuple(a)  # Convert list to tuple so it can be used as a dictionary key
            if a not in res:
                res[a] = [s]  # If key doesn't exist, create a new group
            else:
                res[a].append(s)  # If key exists, add word to the existing group

        return list(res.values())  # Return all grouped anagrams
