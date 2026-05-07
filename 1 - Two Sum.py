class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        a+b=target
        b=target-a
        '''
        hmap={}
        for i in range(len(nums)):
            a=nums[i]
            b=target-a
            if b in hmap:
                return [i,hmap[b]]
            hmap[a]=i
        

        
