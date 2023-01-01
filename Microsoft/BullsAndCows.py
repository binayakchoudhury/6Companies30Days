class Solution :
    def getHint (self , secret : str , guess : str) -> str :
        bulls , cows = 0 , 0
        bucket = [0] * 10

        for s , g in zip (secret , guess) :
            if s == g : 
                bulls += 1

            bucket[int(s)] += 1
            bucket[int(g)] -= 1

        for b in bucket :
            if b > 0 :
                cows += b

        return f'{bulls}A{len(secret) - bulls - cows}B'
