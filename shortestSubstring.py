def get_shortest_unique_substring(arr, str):
    def hasAll(s, arr):
        for i in arr:
            if i not in s: return False
        return True 
    
    
    for i in arr:
        if i not in str: return ""
    
    res = str

    p0, p1 = 0, 1
    n = len(str) - 1
    while p0 <= n and p1 <= n:
        
        if hasAll(str[p0:p1+1], arr) != True:
            p1 += 1
        else: 
            if len(str[p0:p1+1]) < len(res):
                res = str[p0:p1+1]
            p0 += 1

    return res

arr = ['x','y','z']

str = "xyyzyzyx"
print(get_shortest_unique_substring(arr, str))