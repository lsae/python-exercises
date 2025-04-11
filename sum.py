def twoSum(numbers, target):
    nums = {}
    for i, val in enumerate(numbers):
      if target - val in nums:
        return [nums[target - val], i]
      else:
        nums[val] = i
