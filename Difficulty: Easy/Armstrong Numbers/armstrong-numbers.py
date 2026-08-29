class Solution:
    def armstrongNumber (self, n):
        # code here 
        temp=n
        total=0
        while temp>0:
            digit=temp%10
            total+=digit**3
            temp//=10
        return total ==n