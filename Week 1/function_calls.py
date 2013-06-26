fruit = ['apple','orange','grape','kiwi','orange','apple']

# reports the frequency of every item in a list
def analyze_list(l):
  
  counts = {}
  for item in l:
    if item in counts:
      counts[item] = counts[item] + 1
    else:
      counts[item] = 1
      
  return counts
  
  
# let's analyze a list
counts = analyze_list(fruit)
print counts
