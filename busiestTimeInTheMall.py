def find_busiest_period(data):
  most_people = 0
  busiest_timestamp = None
  
  if not data:
    return None
  
  current = 0
  begin = 0
  for end in range(len(data)):
    timestamp, customers, entering = data[end]
    
    if timestamp != data[begin][0]:
      if current > most_people:
        most_people = current
        busiest_timestamp = data[begin][0]
      begin = end
      
    current += customers * (1 if entering else -1)
    current = max(current, 0)
    
  if current > most_people:
    return data[begin][0]
  return busiest_timestamp

test_input = [
  [1487799425, 14, 1], 
  [1487799425, 4,  0],
  [1487799425, 2,  0],
  [1487800378, 10, 1],
  [1487801478, 18, 0],
  [1487801478, 18, 1],
  [1487901013, 1,  0],
  [1487901211, 7,  1],
  [1487901211, 7,  0]
]
print(find_busiest_period(test_input))


"""
  [1487799425, 14, 1], 
  [1487799425, 4,  0],
  [1487799425, 2,  0],
  [1487800378, 10, 1],
  [1487801478, 18, 0],
  [1487801478, 18, 1],
  [1487901013, 1,  0],
A [1487901211, 7,  1],
  [1487901211, 7,  0],
 B
 
current = ?
result = max(result, current) # not returning the max number of people, but the timestamp
"""