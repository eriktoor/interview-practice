class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        res = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p)-1])
        for i in range(len(p)-1,len(s)):
            sCounter[s[i]] += 1   # include a new char in the window
            if sCounter == pCounter:    # This step is O(1), since there are at most 26 English letters 
                res.append(i-len(p)+1)   # append the starting index
            sCounter[s[i-len(p)+1]] -= 1   # decrease the count of oldest char in the window
            if sCounter[s[i-len(p)+1]] == 0:
                del sCounter[s[i-len(p)+1]]   # remove the count if it is 0
        return res
    
    def findAnagramsCounter(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        
        res = []
        from collections import Counter
        hmap_p = Counter(p)
        hmap_s = {}
        n = len(p)
        

        p1 = 0 
        while p1 + n <= len(s): 
            hmap_s = Counter(s[p1:p1+n])
            if hmap_s == hmap_p:
                res.append(p1)

            p1 += 1
        
        return res
    
    def findAnagramsSLOW(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        
        res = []
        sorted_lst = list(p)
        sorted_lst.sort()
        n = len(sorted_lst)
        
        p1 = 0 
        while p1 + n <= len(s): 
            curr = list(s[p1: p1 + n])
            curr.sort()
            if curr == sorted_lst:
                res.append(p1)
            p1 += 1
        
        return res