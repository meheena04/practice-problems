class Solution:
    def firstNonRepeating(self, arr): 
        # Complete the function
        di={}
        res=[]
        m=0
        for i in arr:
            di[i]=di.get(i,0)+1
        for k,v in di.items():
            if v==1:
                m=max(m,k)
                
            res.append(v)
        if 1 not in res:
            return 0
        return m
    
