# Author: Darius Strasel

def find_winners(guess_map):

    def calculate_answer():
        for possible_answer in range(50, 70):
            three_off = 0
            four_off = 0
            for guess in guess_map.values():
                if possible_answer == guess + 3 or possible_answer == guess - 3:
                    three_off += 1
                elif possible_answer == guess + 4 or possible_answer == guess - 4:
                    four_off += 1
            if three_off == 2 and four_off == 1:
                print("Answer found!")
                return possible_answer

    winner_value = min(guess_map.values(), key=lambda x: abs(x - calculate_answer()))
    winners = [person for person in guess_map.keys() if guess_map[person] == winner_value]
    print("Winner(s) is/are %s!" % (", ".join(winners)))

# Now with Bob
find_winners({'daniel': 55, 'arnold': 59, 'eliza': 61, 'bob': 61, 'connor': 65, 'betty': 66})