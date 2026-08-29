class Solution:
    def checkStatus(self, a, b, flag):
        
        if not flag and ((a >= 0 and b < 0) or (a < 0 and b >= 0)):
            return True
        
        if flag and (a < 0 and b < 0):
            return True
            
        return False