import math


greater_than_million = 0
for total in range(1, 101):
	for selected in range(1, total):
		n_combinations = math.factorial(total) / (math.factorial(selected) * math.factorial(total - selected))
		if n_combinations > 10**6:
			greater_than_million += 1

print(greater_than_million)
