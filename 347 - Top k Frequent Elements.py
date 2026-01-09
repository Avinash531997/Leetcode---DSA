class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums) #Count occurences of each element in nums
        freq=[[] for i in range(len(nums)+1)] #Place holder for frequency->n
        for key,v in count.items():
            freq[v].append(key) #Bucket Sort
        result=[]
        for i in range(len(freq)-1,0,-1):
            for ele in freq[i]:
                result.append(ele)
                if(len(result)==k):
                    return result
