class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        first_pointer = 0
        second_pointer = 0
        prev = 0
        if(len(typed) < len(name)):
            return False
        while(second_pointer < len(typed) or first_pointer < len(name)):
            if(first_pointer < len(name) and second_pointer < len(typed) and typed[second_pointer] == name[first_pointer]):
                prev = first_pointer
                first_pointer += 1
                second_pointer += 1
            elif(second_pointer < len(typed) and typed[second_pointer]== name[prev]):
                second_pointer += 1
            else:
                return False
        return True