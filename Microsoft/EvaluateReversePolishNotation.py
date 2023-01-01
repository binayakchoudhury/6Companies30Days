class Solution :
    def evalRPN (self , tokens : List[str]) -> int :
        stacks = []

        for t in tokens :
            if t not in ['+' , '-' , '/' , '*'] :
                stacks.append(int(t))
            else :
                r , l = stacks.pop() , stacks.pop()
                
                if t == "+" :
                    stacks.append(l + r)
                elif t == "-" :
                    stacks.append(l - r)
                elif t == "*" :
                    stacks.append(l * r)
                else :
                    stacks.append(int(float(l) / r))

        return stacks.pop()
