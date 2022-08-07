from typing import List

def twoSum(nums:List [int], target:int):

   dict = { }
   for i, num in enumerate(nums):
      difference = target - num
      if difference in dict:
         print([dict[difference],i])
      else:
         dict[num]=i
         

twoSum([1,2,1,2], 4)
twoSum([1, 2, 3], 4)
twoSum([2, 7, 11, 15], 9)
twoSum([3, 2, 4], 6)
twoSum([3, 3], 6)
 







