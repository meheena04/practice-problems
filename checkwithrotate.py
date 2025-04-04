class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        l=len(mat[0])
        
        for i in range(0,4):
            for i in range(0,l):
                for j in range(i+1,l):
                    mat[i][j],mat[j][i]=mat[j][i],mat[i][j]

            for i in range(0,l):
                mat[i]=mat[i][::-1]
            if mat==target:
                #return True
                break
        if mat!=target:
            return False
        else:
            return True   

        