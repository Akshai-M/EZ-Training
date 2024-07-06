def Algo():
    capacity = int(input("Capacity:"))
    
    item = list(map(int, input("Item:").split()))
    profit = list(map(int, input("Profit:").split()))
    weight = list(map(int, input("Weight:").split()))
    
    Dict = []
    for i in range(len(item)):
        ratio = profit[i] / weight[i]
        Dict.append((item[i], profit[i], weight[i], ratio))
    
    Dict.sort(key=lambda x: x[3], reverse=True)
    # print(Dict)
    total_profit = 0
    knapsack_contents = []
    
    for itm, pft, wt, ratio in Dict:
        print(itm,pft,wt,ratio)
        if capacity >= wt:
            knapsack_contents.append((itm, wt))
            capacity -= wt
            total_profit += pft
        else:
            fraction = capacity / wt
            knapsack_contents.append((itm, wt * fraction))
            total_profit += pft * fraction
            break
    
    print("Total Profit:", total_profit)
    print("Knapsack Contents (item, weight taken):", knapsack_contents)

Algo()