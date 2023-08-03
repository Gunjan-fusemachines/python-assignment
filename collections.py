# task-4 anagrams
def group_anagrams(words):
    anagrams_dict = {}
    for word in words:
        sorted_word = sorted(word, reverse=True)
        sorted_word = ''.join(sorted_word)
        if sorted_word in anagrams_dict:
            anagrams_dict[sorted_word].append(word)
        else:
            anagrams_dict[sorted_word] = [word]

    return list(anagrams_dict.values())

input_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(input_words)
print(result)
