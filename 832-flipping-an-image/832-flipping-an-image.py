class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        i = 0
        for index in image:
            length = len(index)
            for j in range(length//2):
                swap = image[i][j]
                image[i][j] = image[i][length-1-j]
                image[i][length-1-j] = swap
            i += 1
            
        i = 0
        for index in image:
            for j in range(len(index)):
                if(image[i][j] == 1):
                    image[i][j] = 0
                else:
                    image[i][j] = 1
            i += 1
            
        return image
        
        
        
                