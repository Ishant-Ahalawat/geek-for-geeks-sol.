class Solution:
    def reverseDigits(self, n):
        # Code here
        rev=0
        while n>0:
            rev = rev*10 +n%10
            n//=10
        return rev