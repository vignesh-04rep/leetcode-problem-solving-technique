#best solution based on dict
#https://pythontutor.com/render.html#mode=display 

d = dict()
        ops = 0
        
        for num in nums:
            if k-num in d and d[k-num] > 0:
                d[k-num] -= 1
                ops += 1
            else:
                if num not in d:
                    d[num] = 1
                else:
                    d[num] += 1

        return ops



