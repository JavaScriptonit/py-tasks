# Example 1:
# from ast import List
from typing import List

nums1 = [2,7,11,15]
target1 = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:
nums2 = [3,2,4]
target2 = 6
# Output: [1,2]

# Example 3:
nums3 = [3,3]
target3 = 6
# Output: [0,1]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print(f'числа: {nums}')
        print(f'таргет: {target}')

        result_array = []
        i = 0
        array_length = len(nums)
        # print(array_length)
        a = int
        b = int
        
        while i != array_length + 1:
            for num in nums:
                if (num + num == target):
                    print(f'iterator: {i}, {num} + {num} = {target}. Это не подходит, так как сумма чисел может быть только с разными индексами!')
                    new_array = nums.copy() 
                    new_array.remove(num)
                    for new_num in new_array:
                        if (num + new_num == target):
                            a = num
                            b = new_num
                            x = nums
                            def char_index_finder(num, nth_appearance):
                                index = -1
                                repeats = 0
                                for i in x:
                                    index += 1
                                    if i == num:
                                        repeats += 1
                                    if repeats == nth_appearance:
                                        return index
                            
                            print(f'1ое число: {a}')
                            print(f'2ое число: {b}')
                            print(f'iterator: {i}, {num} + {new_num} равно {target}. ЭТО ПОДХОДИТ!')
                            result_array.append(char_index_finder(b, 2))
                            result_array.append(nums.index(a))
                            return result_array
                    continue
                if (num + nums[i] != target):
                    print(f'iterator: {i}, {num} + {nums[i]} не равно {target}. Это не подходит!')
                    continue
                if (num + nums[i] == target):
                    a = num
                    b = nums[i]
                    print(f'1ое число: {a}')
                    print(f'2ое число: {b}')
                    print(f'iterator: {i}, {num} + {nums[i]} равно {target}. ЭТО ПОДХОДИТ!')
                    result_array.append(nums.index(b))
                    result_array.append(nums.index(a))
                    return result_array
            i += 1


print(Solution().twoSum(nums1, target1))