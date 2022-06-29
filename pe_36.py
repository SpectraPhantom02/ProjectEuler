
def get_next_palindrome(n, n_digits):

	if n_digits == 1:
		return n + 1 if n < 9 else 11

	if n_digits == 2:
		next_palindrome = n // 10 * 11
		return next_palindrome if next_palindrome > n else next_palindrome + 11