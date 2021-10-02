# def is_anagram(word1,word2):
#     return sorted(word1) == sorted(word2)
def count_letters(string):
    return {l: string.count(l) for l in string}
def is_anagram(string1, string2):
    return count_letters(string1) == count_letters(string2)
    
print(count_letters("hola", "laho"))
