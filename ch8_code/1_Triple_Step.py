## 8-1 ) Triple Step : A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.

# 피보나치 수열과 비슷
# n이 0일떄를 1로 보느냐 0으로 보느냐에 따라 코드가 달라질 듯
# n = 0일때 방법을 1으로 가정

def getPosWayCnt(n):
    way_cnts = [1, 1, 2]
    if n < 3:
        return way_cnts[n]
    for i in range(3, n+1):
        way_cnts.append(sum(way_cnts[i-3:i]))
    return way_cnts[n]
