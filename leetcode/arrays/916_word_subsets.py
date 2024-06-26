# https://leetcode.com/problems/word-subsets/description/

# У вас есть два массива строк words1 и words2.

# Строка b является подмножеством строки a, если каждая буква в b встречается в a, включая их кратность.

# Например, "wrr" является подмножеством "warrior", но не является подмножеством "world". Строка a из слова words1 является универсальной, если для каждой строки b из words2, b является подмножеством a.

# Верните массив всех универсальных строк в words1. Вы можете вернуть ответ в любом порядке.

# Примеры:

# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"] Output: ["facebook","google","leetcode"]

# Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"] Output: ["apple","google","leetcode"]

# Ограничения:

# 1 <= words1.length, words2.length <= 10^4 
# 1 <= words1[i].length, words2[i].length <= 10 
# words1[i] и words2[i] состоят только из строчных букв английского алфавита. 
# Ве строки из words1 уникальны.


from collections import Counter

class Solution:
    # Метод внутри класса для подсчета количества каждого символа в слове
    def count_chars(self, word):
        # Создаем пустой счётчик с помощью класса Counter из модуля collections
        count = Counter()
        # Проходим по каждому символу в слове
        for char in word:
            # Увеличиваем счетчик символа
            count[char] += 1
        print(f"счётчик count = '{count}'")
        return count

    # Метод внутри класса для нахождения универсальных слов
    def wordSubsets(self, words1, words2):
        # Создаем счетчик символов, который будет содержать максимальное количество каждого символа из words2
        max_char_count = Counter()
        # Проходим по каждому слову в списке words2
        for word in words2:
            # Получаем счетчик символов для каждого слова в words2 с помощью метода count_chars
            word_count = self.count_chars(word)
            # Обновляем максимальный счетчик символов для всех слов в words2
            for char, freq in word_count.items():
                # Записываем наибольшее значение частоты символа в max_char_count
                max_char_count[char] = max(max_char_count[char], freq)
        
        # Создаем массив для универсальных слов
        universal = []
        # Проходим по каждому слову в списке words1
        for word in words1:
            # Получаем счетчик символов для текущего слова
            word_count = self.count_chars(word)
            # Проверяем, содержит ли текущее слово все символы из max_char_count
            if all(word_count[char] >= max_char_count[char] for char in max_char_count):
                # Если текущее слово универсальное, добавляем его в список universal
                universal.append(word)
            # Выводим результат для текущего слова
            print(f"Слово '{word}' содержит все необходимые символы: {all(word_count[char] >= max_char_count[char] for char in max_char_count)}")

        return universal

# Примеры использования:
words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]
# words3 = ["l","e"]
# words1 = ["warrior","world"]
# words2 = ["wrr","w","r","wrrr"]

output = Solution().wordSubsets(words1, words2)
print(f"Слово/слова из массива words1, содержащие все слова из массива words2 = '{output}'")

