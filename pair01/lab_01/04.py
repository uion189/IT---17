N = int(input("Кількість поїздок "))
k = int(input("Кількість квитків у пачці "))
p1 = int(input("Вартість одного квитка "))
p2 = int(input("Вартість пачки "))

cost1 = N * p1

n = N // k
j = N % k
cost_mixed = (n * p2) + (j * p1)


a = (N + k - 1) // k
cost2 = a * p2

min_cost = min(cost1, cost_mixed, cost2)

print(min_cost)
