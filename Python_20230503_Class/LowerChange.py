print("영어단어 2개를 입력하세요.")

word1 = input("영어단어 1 : ")
word2 = input("영어단어 2 : ")

english_word = word1 + word2
lower_cast_string = english_word.lower()
word_count = lower_cast_string.count("a")

print(lower_cast_string)
print(word_count)