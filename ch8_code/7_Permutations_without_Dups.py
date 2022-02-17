## 8-7 )Permutations without Dups: Write a method to compute all permutations of a string of unique characters.

def getPermuts(string):
    result = []
    for i, char in enumerate(string):
        rest = string[:i] + string[i+1:]
        subs = [char + sub for sub in getPermuts(rest)] if rest else [char]
        result += subs
    return result