# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.


# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.


# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False

        nums_list = list(f'{x}')

        # length_of_int = len(str(x))
        length_of_int = len(nums_list)
        half_length = math.floor(length_of_int / 2)
        
        # print(f'dlinna chisla - {half_length}')
        i = 0
        for num in range(half_length):
            i += 1
            # print(f'nomer iteracii cikla dlinnoi v razmer chisla - {num} & {i}')
            if (nums_list[num] != nums_list[length_of_int - i]):
                return False
                
        return True
        




x = 1234567890987654321
# x = -121
# x = 10

print(Solution().isPalindrome(x))