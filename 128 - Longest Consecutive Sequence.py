class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setmap=set(nums)
        longest=0
        for ele in setmap:
            L=0
            if ele-1 not in setmap:
                while ele+L in setmap:
                    L+=1
                longest=max(longest,L)
        return longest
        
