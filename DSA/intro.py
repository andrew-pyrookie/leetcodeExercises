# Data Structures is about how data can be stored in different structures
# Algorithms is about how to solve different problems...often by searching thru or manipulating data structures

# 2 kinds of data stuctures-:
   # Primitive data structures - present single values (int, float,bool,characters)
   # Abstract ds - built using primitive data type and provide ore complex and specialized operations
   
prev2 = 0
prev1 = 1

print(prev2)
print(prev1)

for fibo in range(18):
    newFibo = prev1 + prev2
    print(newFibo)
    prev2 = prev1
    prev1 = newFibo