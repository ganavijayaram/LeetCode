class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_rich = 0
        for i in accounts:
            rich = 0
            for j in i:
                rich += j
            if(rich > max_rich):
                max_rich = rich
        return max_rich