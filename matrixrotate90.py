class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m=matrix
        s=set()
        t=0
        l=len(matrix[0])
        #r=np.empty_like(m)
        for i in range(0,l):
            for j in range(0,l):
                cc=frozenset([i,j])
                if cc not in s:
                    t=m[i][j]
                    m[i][j]=m[j][i]
                    m[j][i]=t
                    s.add(cc)
                    #s.add(m[j][i])

        for i in range(0,l):
            m[i]=m[i][::-1]

            

        