
class Solution(object):
    def dfs(self,image,i,j,color,orgcol):
        if i<0 or j<0 or i>=len(image) or j>=len(image[0]) or image[i][j]!=orgcol:
            return

        image[i][j]=color

        self.dfs(image,i+1,j,color,orgcol)
        self.dfs(image,i-1,j,color,orgcol)
        self.dfs(image,i,j+1,color,orgcol)
        self.dfs(image,i,j-1,color,orgcol)

    def floodFill(self, image, sr, sc, color):
        if image[sr][sc]==color:
            return image

        self.dfs(image,sr,sc,color,image[sr][sc])
        return image
