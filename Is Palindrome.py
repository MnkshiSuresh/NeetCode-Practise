class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs =[]
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        string="".join(strs)
        return string==string[::-1]
        
        
