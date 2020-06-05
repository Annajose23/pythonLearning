def maximumToys(prices, k):
    prices = sorted(prices)
    print(prices)
    price_array = []
    for item in prices:
        k -= item
        if k >= 0:
            price_array.append(item)
        else:
            break
    return len(price_array)

print(maximumToys([1, 12, 5, 111, 200, 1000, 10], 50))
