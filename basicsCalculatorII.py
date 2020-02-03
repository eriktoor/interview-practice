class Solution:
    def calculate(self, s: str) -> int: 
        
        S = [] # stack 
        s = s.replace(r' ', "")
        import re 
        nums = re.findall(r'\d+', s)
        ops = re.findall(r'\+|\-|\*|\/', s)
        
        print(nums)
        print(ops)
        
        if len(ops) == 0: return int(nums[0])
        i = 0
        while i < len(ops): # 0 is for nums 0 and 1, 1 is for nums 1 and 2 
            operator = ops[i]
            
            if operator == "+": 
                pass 
            elif operator == "-": 
                nums[i + 1] = int(nums[i+1]) * -1  
            elif operator == "*": 
                nums[i+1] = int(nums[i]) * int(nums[i+1])
                nums[i] = 0
            elif operator == "/": 
                nums[i+1] = int(int(nums[i]) / int(nums[i+1]))
                nums[i] = 0
            i += 1
            
        print(nums)
        res = 0 
        for i in nums:
            res += int(i)
        return res 
            