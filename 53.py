
def maxSubArray( nums: list[int]) -> int:
    huidige_som = float('-inf')
    beste_som = float('-inf')
    for i in range(len(nums)):
        huidige_som = max(nums[i],huidige_som + nums[i])
        beste_som = max(huidige_som,beste_som)
    return beste_som




