class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        index = 0
        while(index<len(nums)):
            if(nums[index]-1 != index):
                if(nums[nums[index]-1] == nums[index]):
                    index += 1
                    #print("if inc index {0} nums {1}: ".format(index, nums))
                    continue
                temp = nums[nums[index]-1]
                nums[nums[index]-1] = nums[index]
                nums[index] = temp
                #print("if index {0} nums {1}: ".format(index, nums))
            else:
                index += 1
                #print("else index {0} nums {1}: ".format(index, nums))
        lst = []  
        for i in range(len(nums)):
            if(i != nums[i]-1):
                lst.append(i+1)
        return lst