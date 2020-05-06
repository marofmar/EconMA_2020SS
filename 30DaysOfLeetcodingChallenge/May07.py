def majorityElem(nums):
    floor_val = half_floor(len(nums))
    dic = record_freq(nums)
    print(dic)
    vals = [v for k,v in dic.items()]
    cand = []
    for i in vals:
        if i > floor_val:
            cand.append(i)
    mx = max(cand)
    
    rev_dic = {v:k for k,v in dic.items()}
    print(rev_dic)
    return rev_dic[mx]
    
        

def half_floor(number):    
    return number/2 # equal or larger than this value. Should be the max out of them 

def record_freq(lst):
    tmp = {}
    for i in lst:
        if i in tmp: 
            tmp[i] += 1
        else:
            tmp[i] = 1
    return tmp # number: frequency

# a =record_freq([3,2,3])
# print(a)

b = majorityElem([3,2,3,3,3,3,3])
print(b)