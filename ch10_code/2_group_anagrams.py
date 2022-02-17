## 10-2) Group Anagrams: Write a method to sort an array of strings so that all the anagrams are next to each other.

from collections import Counter, defaultdict
def groupAnagrams(arr):
    anagram_table = defaultdict(list)
    result = []

    for word in arr:
        anagram_key = str(Counter(word))
        anagram_table[anagram_key] += [word]

    for arr in anagram_table.values():
        result += arr

    return result