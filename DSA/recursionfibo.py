#  Implementation Using Recursion

print(0)
print(1)

def finobacci(prev1, prev2):
    global count
    if count <= 19:
        newFibo = prev1 + prev2
        print(newFibo)
        prev2 = prev1
        prev1 = newFibo
        count += 1
        finobacci(prev1, prev2)
    else:
        return
    
    
finobacci(1,0)