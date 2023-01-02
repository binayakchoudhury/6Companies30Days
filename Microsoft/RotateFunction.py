class Solution :
    def maxRotateFunction (self , nums : List[int]) -> int :
        value = sum(nums)
        check = sum(element * index for index , element in enumerate (nums))
        result = check

        for pivot in range (len(nums) - 1 , -1 , -1) :
            print(check)
            check += value - len(nums) * nums[pivot]
            result = max(check , result)

        return result
