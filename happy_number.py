class Solution:
    def isHappy(self, n: int) -> bool:
        nums = set()
        while True:
            nums.add(n)
            n = sum(int(ch)** 2 for ch in str(n))
            if n == 1:
                return True
            if n in nums:
                return False


class Solution:
    def isHappy(self, n: int) -> bool:
        slow = self.squared(n)
        fast = self.squared(self.squared(n))

        while fast != slow and fast != 1:
            slow = self.squared(slow)
            fast = self.squared(self.squared(fast))
        return fast == 1


    def squared(self, n):
        res = 0
        while n > 0:
            res +=( n % 10) ** 2
            n //= 10
        return res
