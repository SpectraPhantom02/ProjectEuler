
unique_results = set()

for a in range(2, 101):
	for b in range(2, 101):
		unique_results.add(a ** b)

print(f"Number of distinct terms: {len(unique_results)}")