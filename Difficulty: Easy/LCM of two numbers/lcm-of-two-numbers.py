class Solution:
       
    def lcm(self, a, b):
        # code here
        x,y=a,b
        while y:
            x,y=y,x%y
        return (a*b)//x