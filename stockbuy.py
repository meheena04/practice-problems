class Solution(object):
    def maxProfit(self, prices):
        pr=prices
        b=float('inf')
        s=0
        bk=0
        for k,i in enumerate(pr):
            if b>i:
                b=i

            if i-b>s:
                s=i-b
        return s

        

        