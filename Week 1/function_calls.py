fruit = ['apple','orange','grape','kiwi','orange','apple']

# reports the frequency of every item in a list
def analyze_list(l):
  
  counts = {}
  for item in l:
  
    counts[item] = count[item] + 1
    
  return counts
  
  
# let's analyze a list
counts = analyze_list(fruit)
print counts
