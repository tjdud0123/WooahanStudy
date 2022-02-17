## 8-4 ) Power Set: Write a method to return all subsets of a set.

# 방법 1 DP => 이전 조합 + 자기자신 원소
# reduce 사용
def getPowerSet(arr):
    return reduce(lambda result, el: getSubSets(result, el), arr, [[]])
def getSubSets(result, el):
    new_subs = [subset + [el] for subset in result]
    return result + new_subs

# 방법 2 라이브러리 사용
from itertools import combinations
def getPowerSet(arr):
    p_sets = []
    for i in range(len(arr)+1):
        p_sets += [sets for sets in combinations(arr, i)]
    return p_sets