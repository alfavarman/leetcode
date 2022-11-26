stockProfit = [5, 7, 9, 13, 11, 6, 6, 3, 3]
target = 12


def stock_pairs(arr: list, target: int) -> int:
    indexes = len(stockProfit)
    pairs_list = set()
    for i in range(indexes):
        for n in range(i, indexes):
            if stockProfit[i] + stockProfit[n] == target:
                pairs_list.add((stockProfit[i], stockProfit[n]))

    return len(pairs_list)


print(stock_pairs(stockProfit, target))
