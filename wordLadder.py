"""
Approaches: 

Approach: Graph Search

bit --> *it, b*t, bi*

queue = [] 

q = [(beginWord, 1)]

while queueLength != 0: 

  currWord = queue.pop() 

  if [A-Za-z]it in words: 
    append to queue  (currWord, path + 1)
  if b*t in wordS:
    append to queue (currWord, path + 1)
  if bi* in words: 
    append to queue (currWord, path + 1)
  
  if target == word: 
    return path + 1
 
 return ret 
 
 
 
Time: O(M x N), N is words and M is length of words, Space: O(N)
   
  
source = "bit", target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]

    
  


"""


def checkEquality(word1, wordList, idx):
  ret = 0
  
  count = 0 
  for word in wordList: 
    print(word1, word)
    if word[:idx] == word1[:idx] and word[idx + 1:] == word1[idx + 1:] and word != word1:
      return word

  
  return ret 

def shortestWordEditPath(source, target, words):
  """
  @desc given a source and target word, return the minimum number of changes in order to get to the target
  @param source: str
  @param target: str
  @param words: str[]
  @return: int
  """
  #Error Checking
  if not words or target not in words or len(source) != len(target):
    return -1 
  
  ret = -1 

  visited = set()
  
  q = []
  q.append((source, 0))
  # q.pop(0)
  while len(q) != 0: 
    currWord, path = q.pop(0)
    for i in range(len(currWord)): 
      nextWord = checkEquality(currWord, words, i)
      print(q)
      print(nextWord)
      if nextWord and nextWord not in visited:
        if nextWord == target: return path + 1
        visited.add(nextWord)
        q.append((nextWord, path + 1))

  return ret 


source = "no"
target = "go"
words = ["to"]

print(shortestWordEditPath(source, target, words)) #expected -1 


source = "bit"
target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
print(shortestWordEditPath(source, target, words)) #expected 5


"""
      if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        L = len(beginWord)
        dic = defaultdict(list)
        for word in wordList:
            for i in range(L):
                key = word[:i] + '*' + word[i+1:]
                dic[key].append(word)
                # *ot  = [hot]    h*t = [hot], ho*  = [hot] in list woueld be the words that different one 1 character from key
                print(dic.items())
        
      
        visited = {beginWord:True}
        q = [(beginWord, 1)]
        while q:
            currentWord, level = q.pop(0)
            for i in range(L):
                intermediate_word = current_word[:i]  + {} + current_word[i+1:]
                
                
                for word in dic[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word in visited:
                        continue
                    visited[word] = True  
                    q.append((word, level+1))
                



Case 1: 

"bit", "dog", ["but","put","big","pot","pog","dog","lot"]


Case 2:

"no", "go", ["to"]


Case 3: 
"bit", "pog", ["but","put","big","pot","pog","pig","dog","lot"]


Case 6: 
"aa", "bbb", ["ab","bb"]


"""



