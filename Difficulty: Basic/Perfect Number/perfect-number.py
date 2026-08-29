class Solution:
    def isPerfect(self, N):
        fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        
        temp = N
        digit_sum = 0
        
        while temp > 0:
            digit = temp % 10
            digit_sum += fact[digit]
            temp //= 10
            
        return 1 if digit_sum == N else 0