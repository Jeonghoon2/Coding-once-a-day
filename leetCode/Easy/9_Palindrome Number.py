class Solution:
    def isPalindrome(x: int) -> bool:
        
        reverse_str = ''

        x= str(x)
        
        for i in x[::-1]:
            reverse_str += i
        return reverse_str == x


x = 121

print(Solution.isPalindrome(x))