import os
import copy


# General class, overseeing the procedure of reading the file containing the cards,
# applying the needed transformations for them to be easily processed, determining
# the hands' value, and electing a victor

class PokerHandSimulator:

	def __init__(self, filename, n_hands):
		self.filename = filename
		self.n_hands = n_hands

	# assigns numeric values to letters (10, Jack, Queen, King, Ace)
	def _get_transformed_hand(self, hand):
		for i in range(len(hand)):
			if hand[i][0] == "T": hand[i][0] = 10
			if hand[i][0] == "J": hand[i][0] = 11
			if hand[i][0] == "Q": hand[i][0] = 12
			if hand[i][0] == "K": hand[i][0] = 13
			if hand[i][0] == "A": hand[i][0] = 14

			if hand[i][0] not in ["T", "J", "Q", "K", "A"]:
				hand[i][0] = int(hand[i][0])

		hand_ranks = [hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]]
		hand_suits = [hand[0][1], hand[1][1], hand[2][1], hand[3][1], hand[4][1]]

		temp_hand = [(hand_ranks[i], hand_suits[i]) for i in range(len(hand_ranks))]
		temp_hand.sort(key= lambda x: x[0])

		hand_ranks = [temp_hand[0][0], temp_hand[1][0], temp_hand[2][0], temp_hand[3][0], temp_hand[4][0]]
		hand_suits = [temp_hand[0][1], temp_hand[1][1], temp_hand[2][1], temp_hand[3][1], temp_hand[4][1]]

		return (hand_ranks, hand_suits)


	def _calculate_hand_value(self, hand_ranks, hand_suits):
		

		if self._is_royal_flush(hand_ranks, hand_suits)[0]:
			return (10, self._is_royal_flush(hand_ranks, hand_suits)[1])

		if self._is_straight_flush(hand_ranks, hand_suits)[0]:
			return (9, self._is_straight_flush(hand_ranks, hand_suits)[1])

		if self._is_four_of_kind(hand_ranks, hand_suits)[0]:
			return (8, self._is_four_of_kind(hand_ranks, hand_suits)[1])

		if self._is_full_house(hand_ranks, hand_suits)[0]:
			return (7, self._is_full_house(hand_ranks, hand_suits)[1])

		if self._is_flush(hand_ranks, hand_suits)[0]:
			return (6, self._is_flush(hand_ranks, hand_suits)[1])

		if self._is_straight(hand_ranks, hand_suits)[0]:
			return (5, self._is_straight(hand_ranks, hand_suits)[1])

		if self._is_three_kind(hand_ranks, hand_suits)[0]:
			return (4, self._is_three_kind(hand_ranks, hand_suits)[1])

		if self._is_two_pair(hand_ranks, hand_suits)[0]:
			return (3, self._is_two_pair(hand_ranks, hand_suits)[1])

		if self._is_one_pair(hand_ranks, hand_suits)[0]:
			return (2, self._is_one_pair(hand_ranks, hand_suits)[1])

		hand_ranks_copy = hand_ranks
		hand_ranks_copy.sort(reverse=True)

		return (1, hand_ranks_copy)


	# separates the read poker hands into lists of lists containing the cards' rank and suit
	def _get_truncated_hand(self, hand):
		truncated_hand = []
		for card in hand:
			rank = card[:-1]
			suit = card[-1:]
			truncated_hand.append([rank, suit])

		return truncated_hand

	# reads the poker hands for each player from the provided file
	def _read_poker_hands(self):
		f = open(self.filename)
		player1_hands = []
		player2_hands = []

		for line in f:
			all_cards = line.split()
			player1_hands.append(all_cards[:5])
			player2_hands.append(all_cards[5:])

		f.close()

		return (player1_hands, player2_hands)


	def _is_player1_winner(self, p1_hand_value, p2_hand_value):
		if p1_hand_value[0] > p2_hand_value[0]:
			return True
		elif p1_hand_value[0] < p2_hand_value[0]:
			return False
			
		for i in range(len(p1_hand_value[1])):
			if p1_hand_value[1][i] > p2_hand_value[1][i]:
				return True
			elif p1_hand_value[1][i] < p2_hand_value[1][i]:
				return False

		return True


	# All functions are made to return a tuple conatining:
	# - a boolean determining whether or not a hand is completed
	# - a list of the highest cards, in order

	# WORKING - Impossible to draw
	def _is_royal_flush(self, hand_ranks, hand_suits):
		highest_cards = [hand_ranks[4]]

		return (self._is_flush(hand_ranks, hand_suits)[0] and hand_ranks[0] == 10, highest_cards)

	# WORKING - Impossible to draw
	def _is_straight_flush(self, hand_ranks, hand_suits):
		highest_cards = [hand_ranks[4]]

		return (self._is_straight(hand_ranks, hand_suits)[0] and self._is_flush(hand_ranks, hand_suits)[0], highest_cards)

	# WORKING - Impossible to draw
	def _is_four_of_kind(self, hand_ranks, hand_suits):
		highest_cards = [hand_ranks[2]]

		return (hand_ranks.count(hand_ranks[0]) == 4 or hand_ranks.count(hand_ranks[4]) == 4, highest_cards)

	# WORKING - Can draw
	def _is_full_house(self, hand_ranks, hand_suits):
		triple_card = hand_ranks[3]
		double_card = (sum(hand_ranks) - triple_card * 3) / 2

		highest_cards = [triple_card, double_card] 

		return (hand_ranks.count(triple_card) == 3 and hand_ranks.count(double_card) == 2, highest_cards)

	# WORKING - Can draw
	def _is_flush(self, hand_ranks, hand_suits):
		highest_cards = [hand_ranks[4]]

		return (hand_suits.count(hand_suits[0]) == 5, highest_cards)

	# WORKING - Can draw
	def _is_straight(self, hand_ranks, hand_suits):
		highest_cards = [hand_ranks[4]]

		return (sorted(hand_ranks) == list(range(min(hand_ranks), max(hand_ranks) + 1)), highest_cards)

	# WORKING - Can draw
	def _is_three_kind(self, hand_ranks, hand_suits):
		triple_card = max(set(hand_ranks), key=hand_ranks.count)

		hand_ranks_copy = copy.copy(hand_ranks)
		for i in range(3):
			if triple_card in hand_ranks_copy:
				hand_ranks_copy.remove(triple_card)

		higher_card = max(hand_ranks_copy)
		lower_card = min(hand_ranks_copy)

		highest_cards = [triple_card, higher_card, lower_card]

		return (hand_ranks.count(triple_card) == 3, highest_cards)

	# WORKING - Can draw
	def _is_two_pair(self, hand_ranks, hand_suits):
		pair1_card = max(set(hand_ranks), key=hand_ranks.count)
		
		hand_ranks_copy = copy.copy(hand_ranks)
		for i in range(2):
			if pair1_card in hand_ranks_copy:
				hand_ranks_copy.remove(pair1_card)
		
		pair2_card = max(set(hand_ranks_copy), key=hand_ranks_copy.count)
		
		for i in range(2):
			if pair2_card in hand_ranks_copy:
				hand_ranks_copy.remove(pair2_card)
		
		higher_card = hand_ranks_copy[0]
		highest_cards = [pair1_card if pair1_card > pair2_card else pair2_card,
						 pair2_card if pair2_card < pair1_card else pair1_card,
						 higher_card]


		return (hand_ranks.count(pair1_card) == 2 and hand_ranks.count(pair2_card) == 2, highest_cards)

	# WORKING - Can draw
	def _is_one_pair(self, hand_ranks, hand_suits):
		pair_card = max(set(hand_ranks), key=hand_ranks.count)

		hand_ranks_copy = copy.copy(hand_ranks)
		for i in range(2):
			if pair_card in hand_ranks_copy:
				hand_ranks_copy.remove(pair_card)

		hand_ranks_copy.sort(reverse=True)
		highest_cards = [pair_card, *hand_ranks_copy]

		return (hand_ranks.count(pair_card) == 2, highest_cards)

	def run(self):
		player_hands = self._read_poker_hands()
		p1_wins = 0

		for i in range(self.n_hands):
			player1_hand_ranks, player1_hand_suits = self._get_transformed_hand(self._get_truncated_hand(player_hands[0][i]))
			player2_hand_ranks, player2_hand_suits = self._get_transformed_hand(self._get_truncated_hand(player_hands[1][i]))
			
			player1_hand_value = self._calculate_hand_value(player1_hand_ranks, player1_hand_suits)
			player2_hand_value = self._calculate_hand_value(player2_hand_ranks, player2_hand_suits)

			if self._is_player1_winner(player1_hand_value, player2_hand_value):
				p1_wins += 1

		print(f"Player 1 won {p1_wins} times out of {self.n_hands}!")

# change working directory to this script
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


FILENAME = "pe_54_poker.txt"
N_HANDS = 1000
poker_simulator = PokerHandSimulator(FILENAME, N_HANDS)
poker_simulator.run()



