class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1)>len(nums2):
            nums1,nums2=nums2,nums1


        m=len(nums1)
        n=len(nums2)
        high=m
        low=0
        while low<=high:
            len_num1=(low+high)//2
            len_num2=(m+n+1)//2-len_num1
            if len_num1==0:
                left_min=float('-inf')
            else:
                left_min=nums1[len_num1-1]

            if len_num1==m:
                left_max=float('inf')
            else:
                left_max=nums1[len_num1]

            if len_num2==0:
                right_min=float('-inf')
            else:
                right_min=nums2[len_num2-1]

            if len_num2==n:
                right_max=float('inf')
            else:
                right_max=nums2[len_num2]

            if left_min<=right_max and right_min<=left_max:
                if (m+n)%2==0:
                    return (max(left_min,right_min)+min(right_max,left_max))/2.0
                else:
                    return max(left_min,right_min)

            elif left_min>right_max:
                high=len_num1-1
            else:
                low=len_num1+1
                
                
s1=Solution()
arr1=[2,2,5]
arr2=[3,3,4]
ans=s1.findMedianSortedArrays(arr1,arr2)
print(f"The median is {ans}")