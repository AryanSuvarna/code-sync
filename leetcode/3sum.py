class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        # sort the nums array so we can use 2-pointer approach
        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums) - 2):
            # if we have seen this value already, move on until we see a new value
            if i != 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            # run 2-sum on the remaining values
            l, r = i + 1, len(sorted_nums) - 1

            while l < r:
                calc = sorted_nums[i] + sorted_nums[l] + sorted_nums[r]

                if calc < 0:
                    l += 1
                elif calc > 0:
                    r -= 1
                else:
                    # append the combination that results in the sum of 0
                    res.append([sorted_nums[i],sorted_nums[l], sorted_nums[r]])

                    # keep updating the left pointer until the left pointer is pointing to a new value
                    l += 1
                    while l < r and sorted_nums[l] == sorted_nums[l - 1]:
                        l += 1
            
        return res