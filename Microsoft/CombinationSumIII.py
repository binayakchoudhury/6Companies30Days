class Solution :
    def combinationSum3 (self , k : int , n : int) -> List[List[int]] :
        result = []

        def solve (index , sum , value) :

            # Base Class
            if len(value) == k :
                if sum == n :
                    result.append(value)
                    return

            # Recursion
            for i in range (index , 9 + 1) :
                if i > n : break
                solve (i + 1 , sum + i , value + [i])

        solve (1 , 0 , [])
        return result
