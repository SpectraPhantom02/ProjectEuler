
def get_periodic_sequence_length(n):

	n_digits = len(str(n))
	dividend = 10 ** n_digits
	occured_dividends = [dividend]

	while True:
		result = dividend // n
		dividend -= (result * n)
		dividend *= 10

		if dividend in occured_dividends:
			return len(occured_dividends) - occured_dividends.index(dividend)

		occured_dividends.append(dividend)


longest_cycle = 0
longest_cycle_num = 0
for i in range(11, 1001):
	cycle_len = get_periodic_sequence_length(i)
	if cycle_len > longest_cycle:
		longest_cycle = cycle_len
		longest_cycle_num = i

print(f"Number with longest recurring cycle in decimal fraction: {longest_cycle_num}")
print(f"Longest recurring cycle in decimal fraction: {longest_cycle}")