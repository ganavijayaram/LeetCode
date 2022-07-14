class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = fast = n
        while(True):
            slow = self.square(slow)
            fast = self.square(fast)
            fast = self.square(fast)
            if(slow == 1 or fast == 1):
                return True
            if(slow == fast):
                return False
            
    def square(self, n):
        tot = 0
        while(n):
            rem = n%10
            n /= 10
            tot += rem**2
        return tot