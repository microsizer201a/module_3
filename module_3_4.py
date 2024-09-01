def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if len(root_word) < len(i):
            for j in range(len(i) - len(root_word) + 1):
                low_root_word = root_word.lower()
                low_i = i.lower()
                if low_root_word == low_i[j:j + len(root_word)]:
                    same_words.append(i)
        if len(root_word) > len(i):
            for j in range(len(root_word) - len(i) + 1):
                low_root_word = root_word.lower()
                low_i = i.lower()
                if low_i == low_root_word[j:j + len(i)]:
                    same_words.append(i)
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)