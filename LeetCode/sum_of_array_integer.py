class Solution(object):
    def twoSum(self, nums, target):
        self.nums=nums
        self.target=target
        output=set()
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    output.update([i,j])
                    
        return list(output)
        
s=Solution()
ans=s.twoSum([3,2,4],6)
print(ans)