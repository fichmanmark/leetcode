from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [0] * n
        for i in range(1, n+1):
            tmp = 0
            if i % 3 == 0:
                tmp = 1
            if i % 5 == 0:
                tmp += 2
            if tmp == 0:
                res[i-1] = str(i)
            elif tmp == 1:
                res[i-1] = 'Fizz'
            elif tmp == 2:
                res[i-1] = 'Buzz'
            else:
                res[i-1] = "FizzBuzz"
        return res




assert Solution().fizzBuzz(3) == ["1","2","Fizz"]
assert Solution().fizzBuzz(5) == ["1","2","Fizz","4","Buzz"]
assert Solution().fizzBuzz(15) == ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]