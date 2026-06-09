class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l=1
        r=max(candies)
        res=0
        while(l<=r):
            mid=(l+r)//2
            child=0
            for candy in candies:
                child+=candy//mid
            if child>=k:
                res=max(res,mid)
                l=mid+1
            else:
                r=mid-1
        return res
