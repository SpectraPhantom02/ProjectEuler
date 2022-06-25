# Jan 1st 1900 was a Monday
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

def is_leap_year(year):

	if year % 400 == 0:
		return True

	if year % 100 == 0:
		return False

	if year % 4 == 0:
		return True

	return False

start_year = 1901
end_year = 2001


days_of_month = {1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335}
leap_days_of_month = {1, 32, 61, 92, 122, 153, 183, 214, 245, 275, 306, 336}
sunday_1st_count = 0

# days of week are marked as: Monday - 0; Tuesday - 1; Wednesday - 2 etc.
first_weekday = 1

for year in range(start_year, end_year):
	first_sunday = 7 - first_weekday if first_weekday < 6 else 1
	is_leap = is_leap_year(year)

	month_days = leap_days_of_month if is_leap else days_of_month
	year_len = 366 if is_leap else 365

	year_sundays = {i for i in range(first_sunday, year_len + 1, 7)}
	sunday_1st_count += len(month_days.intersection(year_sundays))

	first_weekday = (first_weekday + year_len) % 7

print(sunday_1st_count)
