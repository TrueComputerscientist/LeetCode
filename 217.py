def containsDuplicate( nums: list[int]) -> bool:
        if len(nums) != len(set(nums)):
            return True
        return False