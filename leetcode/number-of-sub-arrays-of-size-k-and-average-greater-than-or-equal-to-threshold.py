class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        rolling_count = 0
        valid_subsets = 0
        l = 0
        
        for r in range(len(arr)):
            # window is full so make space for new element
            if r - l == k:
                rolling_count -= arr[l]
                l += 1
            
            rolling_count += arr[r]

            # avg = count / k = threshold => avg = count = threshold * k
            if r - l == k - 1 and rolling_count >= threshold * k:
                valid_subsets += 1
        
        return valid_subsets