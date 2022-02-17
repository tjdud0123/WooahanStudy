## 8-11 ) Coins: Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and pennies (1 cent), write code to calculate the number of ways of representing n cents.

# 맞는지 모르겠음
def solution(amount):
    QUARTER, DIME, NICKEL, PENNY = 25, 10, 5, 1
    coin_units = [QUARTER, DIME, NICKEL, PENNY]
    # 큰 화폐부터 -> 거꾸로 sort
    coin_units = sorted(coin_units, reverse=True)
    return getCoinsWayCnt(coin_units, amount)

def getCoinsWayCnt(coin_units, amount):
    if (amount == 0):
        return 1;

    cnt = 0;
    for unit in coin_units:
        if amount - unit >= 0:
            cnt += nCents(amount - unit)
    return cnt;