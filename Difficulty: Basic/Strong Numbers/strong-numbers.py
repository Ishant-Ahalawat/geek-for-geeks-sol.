class Solution:
    def isStrong(self, n: int) -> bool:
        fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        
        temp = n
        sum_fact = 0
        
        while temp > 0:
            digit = temp % 10
            sum_fact += fact[digit]
            temp //= 10
            
        return sum_fact == n