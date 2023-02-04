def deleteNotEnglish(s):
    ans = ''
    for i in s:
        if chr(97) <= i <= chr(122) or chr(65) <= i <= chr(90) or chr(48) <= i <= chr(57):
            print(i)
            ans += i
    return ans.lower()

class Solution:    
    def isPalindrome(s):

        s = deleteNotEnglish(s)

        if s == '':
            return True

        check = 0
        lenth_s = len(s)-1
    
        while lenth_s > 0:
            if s[check] == s[lenth_s]:
                check +=1
                lenth_s -=1
                continue
            else:
                return False
        
        return True

        

print(Solution.isPalindrome("A man, a plan, a canal: Panama"))