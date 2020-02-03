class Solution:
    
    def diStringMatch(self, S): 
        """
        IIIDI 
        012
        
        if i see I:
            empty the stack 
            append num to result
        else:
            append D to result 
        
        """
        
        stack = []
        res = [] 
        
        for i in range(len(S)): 
            if S[i] == "I": 
                res.append(i)
                while len(stack) != 0: 
                    res.append(stack.pop())
            else: 
                stack.append(i)

        res.append(i + 1)

                    
        while len(stack) != 0: 
            res.append(stack.pop())
            
        return res 
    
    def diStringMatch1(self, S):
        lo, hi = 0, len(S)
        ans = []
        for x in S:
            if x == 'I':
                ans.append(lo)
                lo += 1
            else:
                ans.append(hi)
                hi -= 1

        return ans + [lo]        