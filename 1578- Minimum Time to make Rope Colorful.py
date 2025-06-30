class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev=0
        i=0
        res=0
        while(i<len(colors)):
            if i>0 and colors[i]!=colors[i-1]:
                prev=0
            curr=neededTime[i]
            res+=min(prev,curr)
            prev=max(prev,curr)
            i+=1
        return res 


