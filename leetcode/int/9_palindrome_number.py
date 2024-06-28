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


# Решение #1:

import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Проверяем, если число x отрицательное
        if (x < 0):
            return False

        # Преобразуем число x в список символов (цифр)
        nums_list = list(f'{x}')

        # Определяем длину числа (количество цифр)
        length_of_int = len(nums_list)

        # Находим половину длины числа (если число имеет нечетное количество цифр, то центральную цифру не учитываем)
        half_length = math.floor(length_of_int / 2)
        # print(f'dlinna chisla - {half_length}')
        
        i = 0  # Счетчик для перебора цифр в числе
        # Проходим циклом до середины числа
        for num in range(half_length):
            i += 1

            # print(f'nomer iteracii cikla dlinnoi v razmer chisla - {num} & {i}')
            # Сравниваем цифры с обоих концов числа
            if (nums_list[num] != nums_list[length_of_int - i]):
                return False  # Если цифры не совпадают, число не является палиндромом
                
        return True   # Если весь цикл выполнен без возврата False, число является палиндромом


# Решение #2:

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         a = str(x)  # Преобразуем число x в строку a
#         if a == a[::-1]:  # Сравниваем строку a с ее реверсом (обратной записью)
#             return True  # Если строка и ее реверс совпадают, то число является палиндромом
#         return False  # Если строки не совпадают, число не является палиндромом




x = 1234567890987654321
# x = -121
# x = 10

print(Solution().isPalindrome(x))