
# Find first arrangement to have over 10^12 disks, having the exact amount of
# blue disks so that the probability of pulling two blue disks is exactly 50%

total_disk_count = 10 ** 12
is_found = False

while not is_found:
	blue_disk_count = total_disk_count // 2 + 1

	while True:
		
		blue_disk_value = 2 * (blue_disk_count**2 - blue_disk_count)
		total_disk_value = 2 * (total_disk_count**2 - total_disk_count)

		if blue_disk_value < total_disk_count:
			blue_disk_count += 1
			continue

		if blue_disk_value > total_disk_count:
			break

		if_found = True
		print(f"Blue disk count required for 50% odds: {blue_disk_count}")
		break

	total_disk_count += 1