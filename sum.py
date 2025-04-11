def twoSum(self, numbers, sum):
    dict = {}
    for i, val in enumerate(numbers):
      if sum - val in dict:
        return [dict[sum - val], i]
      else:
        dict[val] = i
