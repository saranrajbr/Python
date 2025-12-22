class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #The below code logic is correct but time complexity is o(n^3) but we need o(n^2)
        
        '''
        substring=s[0]
        count=1
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if(s[i:j+1]==s[i:j+1][::-1]):
                    if count<len(s[i:j+1]):
                        count=len(s[i:j+1])
                        substring=s[i:j+1]
        return substring
        '''
        if not s:
            return ""
        first=0
        last=0
        
        def loopcheck(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            # Odd string
            l1, r1 =loopcheck(i, i)

            # Even string
            l2, r2 =loopcheck(i, i + 1)

            if r1 - l1 > last - first:
                first, last = l1, r1
            if r2 - l2 > last - first:
                first, last = l2, r2
                
        return s[first:last+1]
    
    
s=Solution()
ans=s.longestPalindrome("babad")
print(ans)