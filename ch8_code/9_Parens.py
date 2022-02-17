## 8-9 ) Parens: Implement an algorithm to print all valid (e.g., properly opened and closed) combinations of n pairs of parentheses.

def getParens(n):
    parens = [set([]) if i else set(['()']) for i in range(n)]
    
    for i in range(1, n):
        for paren in parens[i-1]:
            for j in range(len(paren)+1):
                new_el = paren[:j] + '()' + paren[j:]
                parens[i].add(new_el)
    return parens[i] if n > 1 else None
