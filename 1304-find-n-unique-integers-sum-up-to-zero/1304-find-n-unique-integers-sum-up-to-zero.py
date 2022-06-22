class Solution:
    def sumZero(self, n: int) -> List[int]:
        output = []
        if(n%2 != 0):
            for i in range(((n//2)+1)-n, n-((n//2)+1)+1):
                output.append(i)
        else:
            for i in range((n//2)-n, n-(n//2)+1):
                if(i!=0):
                    output.append(i)
        return output