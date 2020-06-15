def isPalindrome(s):
    def toChars(s):
        s = s.lower()
        ans = ""
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                ans = ans + c
            return ans
    
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])
            
    print(isPal(s[1:-1]))
    print(s[0] == s[-1] and isPal(s[1:-1]))
    
# This is checking the first and last chars. The function is called again
# at isPal(s[1:-1]), meaning that checking from the 2nd char to the next
# to last char, which is the recursive case.
    return isPal(toChars(s))


print(isPalindrome("ngyyen"))
