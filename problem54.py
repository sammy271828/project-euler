import math
from useful_routines import isTriangle

f = open('poker54.txt')
content = f.read()

class card:
    def __init__(self, value, suit):
        if value == 'T':
            self.value = '10'
        elif value == 'J':
            self.value = '11'
        elif value == 'Q':
            self.value = '12'
        elif value == 'K':
            self.value = '13'
        elif value == 'A':
            self.value = '14'
        else:
            self.value = value

        self.suit = suit

    def print(self):
        print(self.value, self.suit)



class hand:
    def __init__(self, cards):
        self.cards = cards


    def add_card(self, card):
        self.cards.append(card)


    def sorted_values(self):
        values = []
        for i in self.cards:
            values.append(int(i.value))
        values.sort()
        return values


    def print(self):
        arr = []
        for i in self.cards:
            arr.append(i.value + i.suit)
        if len(arr) <= 5:
            print(arr)
        else:
            print("Out of bounds")


    def high_card(self):
        if len(self.cards) == 0:
            return "Empty hand"
        else:
            target = self.cards[0]
            for i in self.cards:
                if int(i.value) > int(target.value):
                    target = i

            return target


    def pair(self):
        values = self.sorted_values()

        for i in range(1,len(values)):
            if values[i] == values[i - 1]:
                return True

        return False


    def two_pair(self):
        values = self.sorted_values()
        pair_count = 0
        i = 0
        while i + 1 < len(values):
            if i + 1 < len(values) and values[i] != values[i + 1]:
                i += 1
            else:
                pair_count += 1
                i += 2

        if pair_count == 2:
            return True
        else:
            return False


    def three_of_kind(self):
        values = self.sorted_values()
        for i in range(0,len(values) - 2):
            if values[i] == values[i + 1] == values[i + 2]:
                return True

        return False


    def straight(self):
        values = self.sorted_values()

        for i in range(0,len(values) - 1):
            if values[i] + 1 != values[i + 1]:
                return False

        return True


    def flush(self):
        suit = self.cards[0].suit
        for i in self.cards:
            if i.suit != suit:
                return False

        return True


    def full_house(self):
        values = self.sorted_values()
        if values[0] == values[2] and values[3] == values[4]:
            return True
        elif values[0] == values[1] and values[2] == values[4]:
            return True
        else:
            return False


    def four_of_kind(self):
        values = self.sorted_values()
        if values[0] == values[3] or values[1] == values[4]:
            return True
        else:
            return False


    def straight_flush(self):
        if self.flush() and self.straight():
            return True
        else:
            return False

    def royal_flush(self):
        if self.straight_flush() and self.high_card().value == '14':
            return True
        else:
            return False


    def rank(self):
        if self.royal_flush():
            return 0
        elif self.straight_flush():
            return 1
        elif self.four_of_kind():
            return 2
        elif self.full_house():
            return 3
        elif self.flush():
            return 4
        elif self.straight():
            return 5
        elif self.three_of_kind():
            return 6
        elif self.two_pair():
            return 7
        elif self.pair():
            return 8
        else:
            return 9



print(content)

cards = []

i = 0

while 3*i < len(content):
    index = 3*i
    value = content[index]
    suit = content[index + 1]
    cards.append(card(value,suit))

    i += 1

hands = []

for i in range(0,1000):
    index = 5 * i
    new_hand = hand([])
    for j in range(0,5):
        new_hand.add_card(cards[index + j])
    hands.append(new_hand)

first = []
second = []

for i in range(0,len(hands)):
    if i % 2 == 0:
        first.append(hands[i])
    else:
        second.append(hands[i])

card = first[3].cards[0]

print(card.value)

print(first[0].cards[2].value)
first[0].high_card().print()


first_wins = 0

for i in range(0,len(first)):
    if first[i].rank() < second[i].rank():
        first_wins += 1
    elif first[i].rank() == second[i].rank() and first[i].high_card().value > second[i].high_card().value:
        first_wins += 1

print(first_wins)