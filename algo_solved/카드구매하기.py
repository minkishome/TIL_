N = int(input())

cards = list(map(int, input().split()))
list_cards = []
for idx, price in enumerate(cards):
    list_cards.append((idx+1, price))
cost = [0] * (N+1)

for idx, price in enumerate(cards):
    for i in range(idx+1, N+1):
        cost[i] = max(cost[i], cost[i - (idx + 1)] + price)

print(cost[-1])

