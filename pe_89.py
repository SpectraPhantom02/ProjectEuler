import os


def get_arabic_numeral(roman_numeral):
	temp_numeral = roman_numeral[::-1]
	arabic_numeral = 0

	last_value = 0
	for i in range(len(temp_numeral)):
		symbol = temp_numeral[i]
		value = 0
		
		if symbol == "I": value = 1
		if symbol == "V": value = 5
		if symbol == "X": value = 10
		if symbol == "L": value = 50
		if symbol == "C": value = 100
		if symbol == "D": value = 500
		if symbol == "M": value = 1000

		if value >= last_value:
			arabic_numeral += value
		else:
			arabic_numeral -= value

		last_value = value

	return arabic_numeral


def generate_optimal_roman_numeral(arabic_numeral):
	roman_numeral = ""

	symbols = ["M", "D", "C", "L", "X", "V"]
	lower_symbols = ["CM", "CD", "XC", "XL", "IX", "IV"]
	values = [1000, 500, 100, 50, 10, 5]
	lower_bounds = [900, 400, 90, 40, 9, 4]

	for i in range(len(symbols)):
		while arabic_numeral >= lower_bounds[i]:

			if arabic_numeral >= values[i]:
				roman_numeral += symbols[i]
				arabic_numeral -= values[i]

			elif arabic_numeral >= lower_bounds[i]:
				roman_numeral += lower_symbols[i]
				arabic_numeral -= lower_bounds[i]
				break

	while arabic_numeral > 0:
		roman_numeral += "I"
		arabic_numeral -= 1

	return roman_numeral


print(generate_optimal_roman_numeral(848))

# change working directory to this script
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


filename = "pe_89_roman.txt"
f = open(filename)
roman_numerals_list = [line for line in f]

characters_saved = 0
for roman_numeral in roman_numerals_list:
	arabic_numeral = get_arabic_numeral(roman_numeral)
	optimal_roman_numeral = generate_optimal_roman_numeral(arabic_numeral)
	char_count = len(roman_numeral)
	optimal_char_count = len(optimal_roman_numeral)

	characters_saved += (char_count - optimal_char_count)

print(f"Total characters saved: {characters_saved}")
print(generate_optimal_roman_numeral(get_arabic_numeral("MDCCCLXXXXV")))
f.close()
