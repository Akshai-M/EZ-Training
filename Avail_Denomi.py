D = [1, 5, 7]
bill = 18
d = {1: 0, 5: 0, 7: 0}

for coin in sorted(D, reverse=True):
    print(coin)
    while bill >= coin:
        bill -= coin
        d[coin] += 1
    if bill == 0:
        break

print(d)
