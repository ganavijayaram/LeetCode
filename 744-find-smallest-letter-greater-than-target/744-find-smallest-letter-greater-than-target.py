class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        start = 0
        end = len(letters) - 1
        while(start <= end):
            mid = start + (end-start)//2
            if(target < letters[mid]):
                end = mid - 1
            elif(target > letters[mid]):
                start =  mid + 1
            else:
                start = mid + 1
                '''
                if(mid == len(letters)-1):
                    return letters[0]
                if(letters[mid+1] == target):
                    start = mid + 1
                else:
                    return letters[mid+1]
                '''
        '''
        if(end == len(letters)-1):
            return letters[0]
        '''
        return letters[(end+1)%len(letters)]