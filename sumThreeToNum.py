# Leetcode 2177

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        def helper_func(num):
            for i in range(num):
                if sum([i, i+1, i+2]) == num:
                    return [i, i+1, i+2]
        
        answer_list = helper_func(num)
        
        if not answer_list:
            return None
        else:
            return answer_list
