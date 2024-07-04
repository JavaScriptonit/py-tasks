# https://leetcode.com/problems/detect-capital/description/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        word_letters = list(word)
        # print(word_letters)
        is_letters_upper = []
        for letter in word_letters:
            is_letters_upper.append(letter.isupper())
        # print(is_letters_upper)
        if all(elem == is_letters_upper[0] for elem in is_letters_upper):
            return True
        if (is_letters_upper[0] == True):
            is_letters_upper.remove(1)
            # print(is_letters_upper)
            if all(elem == False for elem in is_letters_upper):
                return True
            else:
                return False
        else:
            return False


test_word1 = "USA"
test_word2 = "FlaG"
test_word3 = "Flag"
test_word4 = "leetcode"

print(Solution().detectCapitalUse(test_word1))
print(Solution().detectCapitalUse(test_word2))
print(Solution().detectCapitalUse(test_word3))
print(Solution().detectCapitalUse(test_word4))




# Инструкция:

# 1. Создать класс `Solution`, содержащий метод `detectCapitalUse`, который принимает строку `word` и возвращает булевое значение.
# 2. Преобразовать входную строку `word` в список `word_letters` из отдельных символов.
# 3. Создать пустой список `is_letters_upper`, содержащий булевые значения, указывающие, является ли каждый символ в верхнем регистре.
# 4. Проверить, все ли символы в верхнем регистре или все в нижнем регистре:
#    - Если все символы в одном регистре, вернуть `True`.
#    - Если все символы в верхнем регистре, вернуть `True`.
#    - Если первая буква в верхнем регистре, а остальные в нижнем, вернуть `True`.
#    - Во всех остальных случаях вернуть `False`.
# 5. Протестировать решение на нескольких тестовых словах: "USA", "FlaG", "Flag", "leetcode".

# После выполнения этих шагов, код должен правильно определять, соответствует ли использование заглавных букв вводу и возвращать ожидаемый результат для каждого тестового слова.