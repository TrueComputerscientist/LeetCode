import math
nums = [1,2,3,4]
def productExceptSelf( nums: list[int]) -> list[int]:
    result = []
    left = 1
    for i in range(len(nums)):
        val = left
        result.append(val)
        left = left*nums[i]
    right = 1
    for i in range(len(result) - 1,-1,-1):
        val = right
        result[i] = result[i]*val
        right = right*nums[i]
    return result

print(productExceptSelf(nums))