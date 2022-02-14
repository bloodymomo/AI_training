def L(nums, i):

    if i == len(nums)-1:
        return 1
    max_len =1
    for j in range(i+1, len(nums)):
        if nums[j]> nums[i]:
            max_len = max(max_len, L(nums,j)+1)
        return max_len

def cal(nums):
    return max(L(nums, i) for i in range(len(nums)))

print(cal([1,5,2,4,3]))