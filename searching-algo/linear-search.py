arr = [1,2,3,4,5]

def linear_search(nums,target):
    for num in nums:
        if num == target:
            return True
    return False

print(linear_search(arr,1))