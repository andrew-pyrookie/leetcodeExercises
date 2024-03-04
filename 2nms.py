class Solution(object):
    def addTwoNumbers(self, l1, l2):
        ans =[]
 
        for i in range(len(l1)):
            for j in range(len(l2)):
                if l1[i] + l2[j] < 10:
                    ans.append(l1[i] + l2[j])
                else:
                    ans.append(l1[i] + l2[j] % 10)
                    l1[i + 1]
                    
                

        
        return ans

        

l1 = [2,4,3]
l2 = [5,6,4]

solution_objct = Solution()
result = solution_objct.addTwoNumbers(l1, l2)
print(result)