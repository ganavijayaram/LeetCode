# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        start = 0
        end = mountain_arr.length() - 1
        output = []
        first_mid = start + (end-start)//2
        #search in ascending part
        while(start<=end):
            mid = start + (end-start)//2
            mid_value = mountain_arr.get(mid)
            if(mid_value > mountain_arr.get(mid+1)):
                if(first_mid < mid):
                    first_mid = mid
                if(end != mid):
                    end = mid
                else:
                    if(target == mid_value):
                        return mid
                    start = mid + 1
            else:
                if(mid > first_mid):
                    first_mid = mid
                if(target == mid_value):
                    output.append(mid)
                    return mid
                elif(target > mid_value):
                    start = mid + 1
                else:
                    end = mid - 1
                #end = mid
        start = first_mid
        end = mountain_arr.length() - 1
        #Search in the descending part
        while(start <= end):
            mid = start + (end-start)//2
            mid_value = mountain_arr.get(mid)
            if( mid+1 <= end):
                if(mid_value > mountain_arr.get(mid+1)):
                    if(target ==  mid_value):
                        output.append(mid)
                        return mid
                    elif(target >  mid_value):
                        end = mid - 1
                    else:
                        start = mid + 1
                else:
                    start = mid + 1
            else:
                if(target ==  mid_value):
                    output.append(mid)
                    return mid
                elif(target >  mid_value):
                    end = mid - 1
                else:
                    start = mid + 1
                
        return -1