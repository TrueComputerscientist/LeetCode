import math

def maxProduct( nums: list[int]) -> int:
    currProduct = nums[0]
    minProduct = nums[0]
    oldMinProduct = nums[0]
    bestProduct = nums[0]
    for i in range(1,len(nums)):
        oldMinProduct = minProduct
        minProduct = min(minProduct*nums[i],currProduct*nums[i],nums[i])
        currProduct = max(currProduct*nums[i], oldMinProduct*nums[i],nums[i])
        bestProduct = max(bestProduct,currProduct)
    return bestProduct

