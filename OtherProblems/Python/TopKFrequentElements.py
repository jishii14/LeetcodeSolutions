class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numhash = dict()
        
        for n in nums:
            if (not n in numhash):
                numhash[n] = 1
            else:
                numhash[n] += numhash[n]
                
        return heapq.nlargest(k, numhash.keys(), key=count.get)