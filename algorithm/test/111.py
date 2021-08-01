from collections import Counter

word_list = ["123", "테스트", "test", "123", "테스트", "test123", "중복", "중복"]
result = Counter(word_list)
print(result)