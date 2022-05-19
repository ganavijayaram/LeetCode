class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        i = 0
        for index in image:
            length = len(index)
            if(length % 2 == 0):
                k = length//2
            else:
                k =(length//2)+1
            for j in range(k):
                swap = image[i][j] ^ 1
                image[i][j] = image[i][length-1-j] ^ 1
                image[i][length-1-j] = swap
            i += 1
        return image
    
        
        
        
                
        
        
        
                