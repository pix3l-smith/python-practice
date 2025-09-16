from random import choice

tarot = { 1: "The Magician", 2:	"The High Priestess", 3: "The Empress", 4: "The Emperor", 5: "The Hierophant", 6: "The Lovers", 7: "The Chariot", 8: "Strength", 9: "The Hermit", 10: "Wheel of Fortune", 11: "Justice", 12: "The Hanged Man", 13: "Death", 14: "Temperance", 15: "The Devil", 16: "The Tower", 17: "The Star", 18: "The Moon", 19: "The Sun", 20: "Judgement", 21: "The World", 22: "The Fool"}

random_card = choice(list(tarot.keys()))

spread = {}
for time in ["past", "present", "future"]:
    card = choice(list(tarot.keys()))  # pick a fresh random card
    spread[time] = tarot.pop(card)

for time, card in spread.items():
  print(f"Your {time} is the {card} card.")
