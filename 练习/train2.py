def majorityElement(nums) -> int:
    d = {}
    for i in nums:
            d[i] =1
    
    for i in nums:
            d[i] +=1 
    
    for k in d.keys():
        if d[k] > len(nums)//2:
            return k

print(majorityElement([3,2,3]))