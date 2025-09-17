letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {letters:points for letters, points in zip(letters, points)}

letter_to_points[" "] = 0

def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points[f"{letter}"]

  return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points)

player_to_words = {
  "player1": ["BLUE", "TENNIS", "EXIT"],
  "wordNerd": ["EARTH", "EYES", "MACHINE"],
  "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
  "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

def play_word(player, word):
  player_to_words[player].append(word)
  return player_to_words

def update_point_totals(player, word):
  play_word(player, word)

  player_to_points[player] = sum(score_word(w) for w in player_to_words[player])

  return player_to_points

player_to_points = {}

for player, words in player_to_words.items():
  player_points = 0

  for word in words:
    player_points += score_word(word)

  player_to_points[player] = player_points

print(player_to_points)

updated = update_point_totals("player1", "apple")
print(updated)
